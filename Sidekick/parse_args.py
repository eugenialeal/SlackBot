import argparse

def parse_args():
    """
    Parses command line arguments for jobs. 
    Available arguments: --recreate, --norefresh, --dryrun, --refreshonly
    Passing no arguments: default behavior
        Truncsert and Tableau Refresh
    --recreate: necessary if table structure changes
        Drop Create and Tableau Refresh
    --recreate --norefresh:
        Drop Create and don't perform Tableau Refresh
    --dryrun: View the full DDL, do not execute statement or refresh tableau
        Print full statement and return
    --refreshonly: Kick the tableau refresh
        Tableau Refresh only
    Examples:
    python3 jobs/debug__command_line_args.py --norefresh --recreate
    Namespace(dryrun=False, norefresh=True, recreate=True, refreshonly=False)
    python3 jobs/debug__command_line_args.py --norefresh
    Namespace(dryrun=False, norefresh=True, recreate=False, refreshonly=False)
    python3 jobs/debug__command_line_args.py
    Namespace(dryrun=False, norefresh=False, recreate=False, refreshonly=False)
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--recreate", help="recreate", action="store_true")
    parser.add_argument("--norefresh", help="no refresh", action="store_true")
    parser.add_argument("--dryrun", help="dryrun", action="store_true")
    parser.add_argument("--refreshonly", help="refreshonly", action="store_true")
    args = parser.parse_args()

    return args

if __name__ == '__main__':
    print(parse_args())
