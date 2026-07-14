import argparse
from pathlib import Path
import sys

def count_notes(vault_path: Path) -> int:
    """
    Count .md files under vault_path, recursively.
    """
    count = 0
    
    for file_path in vault_path.rglob("*.md"):
        if file_path.is_file():
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
            print(f"Error: Vault path {args.vault} does not exist.")
            return
            
        if not vault_path.is_dir():
            print(f"Error: Vault path {args.vault} is not a directory.")
            return
                
        note_count = count_notes(vault_path)
        print(f"Total notes in {args.vault.resolve()}: {note_count}")
        
if __name__ == "__main__":
    main()