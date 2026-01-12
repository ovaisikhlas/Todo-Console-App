#!/usr/bin/env python3
"""
Main entry point for the In-Memory Console Todo App.
Implements the REPL loop for the command-based interface.
"""

from datetime import datetime
from cli import CLI
from todo_manager import TodoManager


def main():
    """
    Main function that starts the todo application.
    """
    print("Welcome to the In-Memory Console Todo App!")
    print("Type 'help' for available commands or 'quit'/'exit' to exit.")

    # Initialize the todo manager and CLI
    todo_manager = TodoManager()
    cli = CLI(todo_manager)

    # REPL loop
    while True:
        try:
            user_input = input("\ntodo> ").strip()

            # Parse the command
            command, args, flags = cli.parse_command(user_input)

            if command is None:
                continue  # Empty input, just continue the loop

            # Process commands
            if command in ['quit', 'exit']:
                print("Goodbye!")
                break
            elif command == 'help':
                cli.display_help()
            elif command == 'add':
                title = cli.get_user_input("Enter task title (required): ").strip()
                if not title:
                    cli.display_error("Title is required!")
                    continue

                description = cli.get_user_input("Enter task description (optional, press Enter to skip): ").strip()
                if not description:  # If empty, set to None
                    description = None

                # Prompt for priority with default shown
                priority_input = cli.get_user_input("Enter priority (high/medium/low, default: medium): ").strip().lower()
                if not priority_input:
                    priority = "medium"  # Default value
                elif priority_input in ["high", "medium", "low"]:
                    priority = priority_input
                else:
                    cli.display_error(f"Invalid priority: '{priority_input}'. Must be one of 'high', 'medium', 'low'.")
                    continue

                # Prompt for tags (comma-separated)
                tags_input = cli.get_user_input("Enter tags (comma-separated, e.g., work,urgent,client): ").strip()
                tags = []
                if tags_input:
                    # Parse tags: split by comma, strip whitespace, prevent duplicates
                    raw_tags = tags_input.split(',')
                    for tag in raw_tags:
                        clean_tag = tag.strip()
                        if clean_tag and clean_tag not in tags:  # Prevent duplicates
                            tags.append(clean_tag)

                # Prompt for due date (optional)
                due_date_input = cli.get_user_input("Enter due date (optional, format: YYYY-MM-DD HH:MM or YYYY-MM-DD, press Enter to skip): ").strip()
                due_date = None
                if due_date_input:
                    try:
                        # Try parsing with time first
                        due_date = datetime.strptime(due_date_input, "%Y-%m-%d %H:%M")
                    except ValueError:
                        try:
                            # Try parsing date only (default to 23:59)
                            date_part = datetime.strptime(due_date_input, "%Y-%m-%d")
                            due_date = date_part.replace(hour=23, minute=59)
                        except ValueError:
                            cli.display_error(f"Invalid date format: '{due_date_input}'. Expected format: YYYY-MM-DD [HH:MM]")
                            continue

                # Prompt for recurrence pattern (optional)
                recurrence_input = cli.get_user_input("Enter recurrence pattern (optional, none/daily/weekly/monthly, press Enter to skip): ").strip().lower()
                if not recurrence_input:
                    recurrence = "none"  # Default value
                elif recurrence_input in ["none", "daily", "weekly", "monthly"]:
                    recurrence = recurrence_input
                else:
                    cli.display_error(f"Invalid recurrence pattern: '{recurrence_input}'. Must be one of 'none', 'daily', 'weekly', 'monthly'.")
                    continue

                task = todo_manager.add_task(title, description, priority, tags, due_date, recurrence)
                cli.display_confirmation(f"Task added with ID {task.id}: {task.title}")
            elif command == 'list':
                # Get all tasks initially
                tasks = todo_manager.list_tasks()

                # Apply search if provided
                if 'search' in flags:
                    keyword = flags['search']
                    tasks = todo_manager.search_tasks(keyword)
                elif len(args) > 0 and args[0]:  # If there's an argument that's not a flag, treat as search
                    keyword = args[0]
                    tasks = todo_manager.search_tasks(keyword)

                # Apply filters
                status = flags.get('status')
                priority_filter = flags.get('priority')
                tags_filter = flags.get('tag')  # This will be a list of tags
                overdue_only = 'overdue' in flags

                # Validate filter values
                if status and status not in ['pending', 'completed', 'all']:
                    cli.display_error(f"Invalid status filter: '{status}'. Must be one of 'pending', 'completed', 'all'.")
                    continue

                if priority_filter and priority_filter not in ['high', 'medium', 'low', 'all']:
                    cli.display_error(f"Invalid priority filter: '{priority_filter}'. Must be one of 'high', 'medium', 'low', 'all'.")
                    continue

                if status or priority_filter or tags_filter or overdue_only:
                    tasks = todo_manager.filter_tasks(status=status, priority=priority_filter, tags=tags_filter, overdue_only=overdue_only)

                # Apply sorting
                sort_criterion = flags.get('sort', 'id')  # Default to 'id' if no sort flag
                if sort_criterion != 'id':
                    if sort_criterion not in ['id', 'priority', 'alpha', 'due']:
                        cli.display_error(f"Invalid sort criterion: '{sort_criterion}'. Must be one of 'id', 'priority', 'alpha', 'due'.")
                        continue
                    tasks = todo_manager.sort_tasks(tasks, sort_criterion)

                # Display results
                if not tasks:
                    print("No tasks match your criteria.")
                else:
                    cli.display_tasks(tasks)
            elif command == 'search':
                if not args:
                    cli.display_error("Please provide a keyword to search for.")
                    continue

                keyword = args[0]
                matching_tasks = todo_manager.search_tasks(keyword)
                cli.display_tasks(matching_tasks)
            elif command == 'update':
                if not args:
                    cli.display_error("Please provide a task ID for update command.")
                    continue

                try:
                    task_id = int(args[0])
                except ValueError:
                    cli.display_error("Task ID must be a number.")
                    continue

                task = todo_manager.get_task_by_id(task_id)
                if not task:
                    cli.display_error(f"No task found with ID {task_id}.")
                    continue

                # Get new title (or keep current if Enter pressed)
                new_title = cli.get_user_input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
                if not new_title:
                    new_title = None  # None means don't update

                # Get new description (or keep current if Enter pressed)
                current_desc = task.description if task.description else ""
                new_desc = cli.get_user_input(f"Enter new description (current: '{current_desc}', press Enter to keep current): ").strip()
                if new_desc == "":  # If user pressed Enter without typing
                    new_desc = None  # None means don't update

                # Get new priority (or keep current if Enter pressed)
                current_priority = task.priority
                new_priority_input = cli.get_user_input(f"Enter new priority (current: '{current_priority}', high/medium/low, press Enter to keep current): ").strip().lower()
                if not new_priority_input:
                    new_priority = None  # None means don't update
                elif new_priority_input in ["high", "medium", "low"]:
                    new_priority = new_priority_input
                else:
                    cli.display_error(f"Invalid priority: '{new_priority_input}'. Must be one of 'high', 'medium', 'low'.")
                    continue

                # Get new tags (or keep current if Enter pressed)
                current_tags = ", ".join(task.tags) if task.tags else ""
                new_tags_input = cli.get_user_input(f"Enter new tags (current: '{current_tags}', comma-separated, press Enter to keep current): ").strip()
                new_tags = None  # None means don't update
                if new_tags_input == "":  # User pressed Enter without typing
                    new_tags = None  # None means don't update
                elif new_tags_input:  # User entered new tags
                    # Parse tags: split by comma, strip whitespace, prevent duplicates
                    raw_tags = new_tags_input.split(',')
                    new_tags = []
                    for tag in raw_tags:
                        clean_tag = tag.strip()
                        if clean_tag and clean_tag not in new_tags:  # Prevent duplicates
                            new_tags.append(clean_tag)
                else:  # User entered empty string to clear tags
                    new_tags = []  # Empty list means clear tags

                # Get new due date (or keep current if Enter pressed)
                current_due_date = task.due_date.strftime("%Y-%m-%d %H:%M") if task.due_date else "None"
                new_due_date_input = cli.get_user_input(f"Enter new due date (current: '{current_due_date}', format: YYYY-MM-DD HH:MM or YYYY-MM-DD, press Enter to keep current, or 'clear' to remove): ").strip()
                new_due_date_str = None  # None means don't update
                if new_due_date_input == "":  # User pressed Enter without typing
                    new_due_date_str = None  # None means don't update
                elif new_due_date_input.lower() == "clear":  # User wants to clear the due date
                    new_due_date_str = ""  # Empty string means clear the due date
                elif new_due_date_input:  # User entered a new due date
                    # Validate the date format before passing to the update method
                    try:
                        # Try parsing with time first
                        datetime.strptime(new_due_date_input, "%Y-%m-%d %H:%M")
                        new_due_date_str = new_due_date_input  # Pass the original string to the update method
                    except ValueError:
                        try:
                            # Try parsing date only (default to 23:59)
                            datetime.strptime(new_due_date_input, "%Y-%m-%d")
                            new_due_date_str = new_due_date_input  # Pass the original string to the update method
                        except ValueError:
                            cli.display_error(f"Invalid date format: '{new_due_date_input}'. Expected format: YYYY-MM-DD [HH:MM]")
                            continue
                else:  # Empty string means clear the due date
                    new_due_date_str = ""  # Empty string means clear the due date

                # Get new recurrence pattern (or keep current if Enter pressed)
                current_recurrence = task.recurrence
                new_recurrence_input = cli.get_user_input(f"Enter new recurrence pattern (current: '{current_recurrence}', none/daily/weekly/monthly, press Enter to keep current): ").strip().lower()
                new_recurrence = None  # None means don't update
                if not new_recurrence_input:  # User pressed Enter without typing
                    new_recurrence = None  # None means don't update
                elif new_recurrence_input in ["none", "daily", "weekly", "monthly"]:  # Valid recurrence pattern
                    new_recurrence = new_recurrence_input
                else:
                    cli.display_error(f"Invalid recurrence pattern: '{new_recurrence_input}'. Must be one of 'none', 'daily', 'weekly', 'monthly'.")
                    continue

                updated_task = todo_manager.update_task(task_id, new_title, new_desc, new_priority, new_tags, new_due_date_str, new_recurrence)
                if updated_task:
                    cli.display_confirmation(f"Task {task_id} updated successfully.")
                else:
                    cli.display_error(f"Failed to update task {task_id}.")
            elif command == 'delete':
                if not args:
                    cli.display_error("Please provide a task ID for delete command.")
                    continue

                try:
                    task_id = int(args[0])
                except ValueError:
                    cli.display_error("Task ID must be a number.")
                    continue

                deleted = todo_manager.delete_task(task_id)
                if deleted:
                    cli.display_confirmation(f"Task {task_id} deleted successfully.")
                else:
                    cli.display_error(f"No task found with ID {task_id}.")
            elif command == 'complete':
                if not args:
                    cli.display_error("Please provide a task ID for complete command.")
                    continue

                try:
                    task_id = int(args[0])
                except ValueError:
                    cli.display_error("Task ID must be a number.")
                    continue

                task = todo_manager.toggle_task_completion(task_id)
                if task:
                    status = "complete" if task.completed else "incomplete"
                    cli.display_feedback(f"Task {task_id} marked as {status}.")
                else:
                    cli.display_error(f"No task found with ID {task_id}.")
            else:
                cli.display_error(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()