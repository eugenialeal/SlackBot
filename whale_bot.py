import os
import sys
import pandas as pd
from tabulate import tabulate
from slack import WebClient
from sidekick.alchemy import mw_headless
from sidekick.enhance import timeit, post_influx
from sidekick.parse_args import parse_args

__author__ = 'Eugenia Leal'
__copyright__ = 'November 2022 Operation Harpoon'
__credits__ = ''
__license__ = ''
__version__ = '2.0.0'
__status__ = 'in_progress'
__maintainer__ = 'Eugenia Leal'
__email__ = ['eleal@bettercollective.com',
             'ecleal10@gmail.com']

@timeit
@post_influx(file=sys.argv[0])
def main():
  
  print("work in progress")

#     cl_args = parse_args()
#     mw = mw_headless()
#     slack_client = WebClient(token=os.environ['SLACK_TOKEN'])

#     with open(os.environ['ASCRIPTS_HOME'] + '/jobs/eo_ipso/affiliate__summary.sql') as f:
        
#         aff_stage = ''.join(f.readlines()[1:-1]).replace('affiliate.', 'affiliate_stage.')

#     query = f"""
    
#     WITH x AS (
#       SELECT 
#       DATE_TRUNC('day',p.created_at AT TIME ZONE 'america/new_york')::date AS date_of_bet,
#       p.user_id,
#       u.name AS users_name,
#       'single bet' AS type_of_bet,
#       b.display_name,
#       l.name AS league,
#       p.money
#       WHERE tandb.picks p
#       JOIN tandb.books b on p.book_id = b.id
#       JOIN tandb.leagues l on p.league_id = l.id
#       JOIN tandb.users u on p.user_id = u.id

#       WHERE is_synced = true
#       AND group_pick_id is null
#       AND parent_name = 'PointsBet'
#       ),

#       get_percentage as (
#       SELECT *,
#       NTILE(1000) OVER (ORDER BY money DESC) as percentiles
#       FROM x 
#       ORDER BY 7 ASC)

#       SELECT date_of_bet,
#       user_id,
#       users_name,
#       type_of_bet,
#       display_name,
#       league,
#       money,
#       row_number() over (order by money desc) AS rank
#       FROM get_percentage 
#       WHERE percentiles = 1
#       ORDER BY money DESC
#       """
  
