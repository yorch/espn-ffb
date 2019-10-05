# espn-ffb
espn-ffb is a project to query fantasy football data from ESPN's API and persist it in your own database. There is a very basic web component with a few views built using Flask that allows you to self-host your own fantasy football league page.

#### Pre-requisites:
*  [Python3](https://www.python.org/download/releases/3.0/)
*  [PostgreSQL](https://www.postgresql.org/download/)
*  uWSGI (optional, but recommended if running in production)

Until all [raw SQL is converted to ORM](https://github.com/raphattack/espn-ffb/issues/1), this will only work with PostgreSQL for now, but you can modify the queries in [query.py](espn_ffb/db/query.py) to work with other databases supported by [SQLAlchemy](https://docs.sqlalchemy.org/en/13/core/engines.html).

## Sample views:
*  Recap - [desktop](sample/images/recap-desktop.png), [mobile](sample/images/recap-mobile.png)
*  Standings - [desktop](sample/images/standings.png)
*  Head-to-head records - [mobile](sample/images/h2h-records.png)
*  Matchup history - [mobile](sample/images/matchup-history.png)
*  Playoffs - [desktop](sample/images/playoffs.png)

## Requirements:
```
pip3 install -r requirements.txt
```

## Config:

Edit [config.py](espn_ffb/config.py) with your own:
*  Database credentials in `DevConfig` and `ProdConfig`.
*  `LEAGUE_ID`
*  `swid` (private leagues)
*  `espn_s2` (private leagues)
  
To find your `swid` and `espn_s2` in Chrome, go to **DevTools > Application > Cookies >** https://fantasy.espn.com.

## Setup:
```
python3 -m espn_ffb.setup -e {dev|prod}
```

## Run:
```
# run with python3
python3 -m espn_ffb.app -e {dev|prod}

# run with uwsgi
uwsgi --http 0.0.0.0:5000 --ini conf/espn-ffb-{dev|prod}.ini
```

## Update:
```
python3 -m espn_ffb.db.update -e {dev|prod}
```

## Build:
```
./gradlew clean build buildDeb -PbuildNumber=local
```

## Install:
```
sudo dpkg -i build/distributions/espn-ffb*.deb
```

The `.deb` package includes two `.service` files:
*  `espn-ffb.service`: Starts espn-ffb Flask app
*  `espn-ffb-update.service`: Updates espn-ffb database

## Recaps:
Sample [recap templates](espn_ffb/templates/recap/2018/2) as an example of how to structure written recaps. 

### Generate a new blank recap template:
```
python3 -m espn_ffb.scripts.generate_recap -e {dev|prod} -y {year} -w {week}
```
