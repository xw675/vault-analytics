import argparse
from pathlib import Path
import sys
import os

def count_notes(vault_path: Path) -> int:
    """
    Count .md files under vault_path, recursively.
    Skip directories starting with a dot (hidden directories).
    """
    count = 0
    
    for root, dirs, files in os.walk(vault_path):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md') and not file.startswith('.'):
                count += 1
                
    return count

def main() -> None:
    """argparse setup: one subparser 'stats' with a --vault PATH option; dispatch to count_notes and print."""
    parser = argparse.ArgumentParser(description="Vault CLI Utility")
    subparsers = parser.add_subparsers(dest="command", required=True)

    stats_parser = subparsers.add_parser("stats", help="Get statistics about the vault")
    stats_parser.add_argument("--vault", required=True, type=Path, help="Path to the vault directory")

    args = parser.parse_args()

    if args.command == "stats":
        vault_path = args.vault
        if not vault_path.exists():
            print(f"Error: Vault path {args.vault} does not exist.", file=sys.stderr)
            sys.exit(1)
            
        if not vault_path.is_dir():
            print(f"Error: Vault path {args.vault} is not a directory.", file=sys.stderr)
            sys.exit(1)
            
        note_count = count_notes(vault_path)
        print(f"Total notes in {args.vault.resolve()}: {note_count}")
        
if __name__ == "__main__":
    main()