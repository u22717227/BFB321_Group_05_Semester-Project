# Eyabantu Taxi Program - BFB 321 Group 05

## Project Description
Eyabantu ("for the people") is a mobile-first web application that brings real-time visibility to South Africa's minibus taxi industry, which carries 65-75% of the country's public transport users.

- **Commuters** can see where taxis stop on 6 pilot routes into Pretoria CBD, when the next taxi will arrive, and which problems have been reported at taxi ranks.
- **Drivers and taxi associations** can see where passenger demand is highest and how many spare taxis to send where.
- **Everyone** can report stops, safe pickups and how safe they felt, which is how stops get verified.

Stops are verified by combining driver GPS, commuter reports and existing route data. The website includes an SOS button that calls the police (10111) for commuters who feel unsafe.

*BFB 321 Supply Chain Web Application - Semester Project (Step 1: Frontend Build, Step 2: Supply Chain Model). Built with HTML, CSS and Python only.*

## Group 05 Members
| **Name**          | **Student Number** |
|-------------------|--------------------|
| Danie Smit        | u23596717          |
| Harley Dalmeida   | u22717227          |
| Jaco Grobbelaar   | u23535173          |

## Installation and Setup

### What you need
- **Python 3.8 or newer**: download from python.org (on Windows, tick "Add Python to PATH" during install)
- **A web browser**: Chrome, Edge, Firefox or Safari
- **VS Code** (recommended)
- **Git** (only needed to clone from GitHub)

### Step 1: Get the project
Either clone it from GitHub:
```
git clone [https://github.com/u22717227/BFB321_Group_05_Semester-Project.git](https://github.com/u22717227/BFB321_Group_05_Semester-Project.git)
cd BFB321_Group_05_Semester-Project
```
or download the zip, **right-click it and choose "Extract All"**, and open the extracted folder.

> **Important:** always extract the whole zip first. Opening a page straight from inside the zip, or copying only the HTML files, shows the page without its colours and photo, because the `static` folder (style.css and taxis.jpg) must sit next to the `templates` folder.

### Step 2: Open it in VS Code
**File > Open Folder** and choose the project folder (the one containing `README.md`, `templates` and `static`).

### Step 3: Set up Python and install the test package
Open a terminal in VS Code (**Terminal > New Terminal**) and run:

**Windows**
```
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
```

**Ubuntu / Linux / Mac**
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Run the supply chain model tests
```
py -m pytest            # Windows
python3 -m pytest       # Ubuntu / Linux / Mac
```
All 7 tests should pass.

### Step 5: Run the model demo
```
py run_eyabantu_demo.py         # Windows
python3 run_eyabantu_demo.py    # Ubuntu / Linux / Mac
```
This prints the ETAs, confidence scores, demand intensity and taxi deployment shown on the website.

### Step 6: Open the website
Double-click **`index.html` in the main project folder**. It forwards to the welcome page (`templates/index.html`). From there, use the buttons in the blocks to reach Live stops, Demand and Report a stop, and the "Back to welcome page" button to return.

No internet connection or extra install is needed for the website.

## Team Contributions

### Danie Smit (u23596717)
- Built the supply chain model with documented formulas (supply_chain_model.py)
- Wrote the unit tests checked against hand calculations (test_supply_chain_model.py)
- Added the model demo script (run_eyabantu_demo.py)

### Harley Dalmeida (u22717227)
- Built the commuter Live Stops page with ETA table, confidence badges and KPI tiles (stops.html)
- Added the "Report a problem" pop-up and the "Current problems at taxi ranks" table (stops.html)
- Built the driver/association Demand heat map page (demand.html)

### Jaco Grobbelaar (u23535173)
- Built the welcome page: hero with taxi photo, stats band, SOS button, user blocks and how-it-works section (index.html)
- Built the Report a Stop form with validation and error messages (report.html)
- Created the shared stylesheet: top bar, buttons, cards, tables, badges, KPI tiles, form errors, pop-up (style.css)
- Added README.md, requirements.txt and .gitignore

## Project Purpose

The minibus taxi industry carries 65% to 75% of South Africa's public transport users, which is about 15 million trips a day across roughly 200 000 to 283 000 taxis. The industry generates around R90 billion a year and employs about 300 000 drivers and 100 000 marshals. It works like a logistics network that moves commuters from residential areas to work, economic and educational destinations.

Despite its size, the industry is informal and unscheduled. Taxis leave only when full, there are no published routes or timetables, and vehicles are not tracked. Commuters wait long and unpredictable times at ranks that can feel unsafe, while drivers chase the same passengers in busy areas and struggle to find customers in off-peak times.

Eyabantu aims to improve customer fulfilment and fleet utilisation by sharing real-time information between commuters, drivers and taxi associations. It builds on existing tools such as TeksiMap and WhereIsMyTransport instead of replacing them.

### Impact Areas:
- **Social:** Shorter waiting times and safer, more predictable waiting at ranks and stops.
- **Economic:** Better use of seats and higher driver income, especially in off-peak hours.
- **Operational:** Route and demand data that associations and municipalities can use for fleet planning.

### Pilot Area
The demo data uses 6 Tshwane routes into Pretoria CBD:

| Route | Stops |
|---|---|
| Mamelodi - Pretoria CBD | Mamelodi Rank, Denneboom |
| Silverton - Pretoria CBD | Silverton |
| Soshanguve - Pretoria CBD | Soshanguve Rank |
| Atteridgeville - Pretoria CBD | Atteridgeville Rank |
| Mabopane - Pretoria CBD | Mabopane Station |
| Hammanskraal - Pretoria CBD | Hammanskraal Rank |

Baseline waiting time, headway, occupancy percentage and demand will be measured on these routes before comparing against Eyabantu.

---

## Features

### Welcome Page (index.html)
- **Sticky header** with the Eyabantu logo on every page; clicking it returns to the welcome page.
- **Hero section**: "Sawubona! Ride smarter with Eyabantu" next to a framed photo of minibus taxis.
- **Stats band** (yellow) with facts from the proposal: 15 million daily trips, 65-75% of public transport users, 6 pilot routes and the 7 taxi stops on them.
- **SOS block**: a red "Call Police 10111" button that dials straight from a phone.
- **"How will you use Eyabantu?"**: three blocks with icons, one per user, each with its own button (View live stops, View demand, Report a stop).
- **How it works**: three steps (commuters report, drivers confirm, everyone benefits).
- **Pilot routes**: the 6 routes, each showing its stops (the Mamelodi route has two: Mamelodi Rank and Denneboom).

### Commuter Features (stops.html)
- **Live Stops table**: Stop, route, ETA and a confidence badge per stop.
- **Verified / Unverified badges**: Stops only show as verified once enough reports agree.
- **KPI tiles**: Expected waiting time, occupancy percentage and number of verified stops.
- **Current problems at taxi ranks**: Numbered table of reported problems per stop, most reported first. The page refreshes itself every 60 seconds (HTML meta refresh, no JavaScript).
- **Report a problem (pop-up)**: Report a late taxi, a moved stop or an unsafe stop from the same page. Built in pure CSS (`:target`), no JavaScript

### Driver & Association Features (demand.html)
- **Demand heat map**: Passengers waiting, taxis present and the demand level per stop, shown in plain words for easy reading: Very high, High, Moderate or Low.
- **Colour code** (with a key above the table): Very high = dark red, High = light red, Moderate = light orange, Low = light green.
- **Deployment advice**: Number of the 20 spare taxis to send to each stop, sorted from most to least under-served.
- **Current reports on stops**: Numbered table of the latest reports from the Report a stop form (stop, route, report type, safety rating and time).
- **Totals**: Passengers waiting now (740) and forecast passengers in the next hour (776).

### Reporting Features (report.html)
- **Report a stop or pickup**: Stop dropdown, route dropdown (6 routes), report type and a 1-5 safety rating.
- **Report types**: Taxi stops here, I was picked up safely, I felt safe while waiting at this stop.
- **Form validation**: Required fields, minimum length and rating range checks.
- **Helpful error messages**: A red message under each field explains what to fix.

### Frontend Design
- **HTML and CSS only**: No JavaScript and no external libraries, so the pages also work offline.
- **Website layout**: Sticky header, full-width sections and a yellow banner at the top of each page.
- **Navigation**: Every page has a clear "Back to welcome page" button at the bottom.
- **Taxi colour theme**: Taxi yellow with charcoal, used for all buttons and highlights.
- **Responsive layout**: Works on phones (the hero image stacks under the text, tables scroll, blocks and KPI tiles stack).
- **Accessibility**: Labels on every input, table captions and headers, alt text on the photo.
- **Reusable components**: One top bar, button, card, table, badge and KPI style shared by all pages.
- **Consistent typography and spacing**: One font and a 16px spacing scale.

### Supply Chain Model (supply_chain_model.py)
A standalone Python module with no Flask or database code. Each function has a docstring with its formula and assumptions.

| Function | Formula | Feedback addressed |
|---|---|---|
| `eta_minutes()` | ETA = d / v x 60 + stops ahead x 1.5 min dwell | How ETA is calculated |
| `expected_wait()` | Average wait = headway / 2 | Passenger waiting time KPI |
| `occupancy_percentage()` | Passengers / seats (15) x 100 | Occupancy KPI |
| `confidence_score()` | (pins + 2 x GPS) / 10, capped at 0.5 if under 3 reports | Low participation, wrong pins, missing GPS |
| `forecast_demand()` | Exponential smoothing: F = a x A + (1 - a) x F | Replaces MPS with a passenger-demand method |
| `demand_intensity()` | Passengers waiting / seats present (above 1 = under-served) | How demand intensity is calculated |
| `demand_level()` | Above 3 = Very high, 1.1-3 = High, 0.8-1.1 = Moderate, below 0.8 = Low | Shows demand in plain words |
| `deploy_taxis()` | Send each spare taxi to the stop with the largest seat shortfall | Turning demand into a deployment decision |

### Testing (test_supply_chain_model.py)
- Unit tests verify each formula against hand calculations (e.g. 5 km at 30 km/h + 2 stops = 13 min)
- Invalid inputs (e.g. zero speed) raise a `ValueError`

### Planned for the Final Project
- Flask API and MySQL database (stops, routes, reports, GPS pings)
- Live data instead of demo values on the pages
- Problem reports saved to the database so the problems table updates for everyone
- Opt-in driver GPS sharing and association logins

---

## Folder Structure
```
BFB321_Group_05_Semester-Project/
|-- index.html                   # start page: opens the welcome page
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- supply_chain_model.py        # standalone model
|-- test_supply_chain_model.py   # unit tests
|-- run_eyabantu_demo.py         # runs the model on demo data
|-- templates/
|   |-- index.html               # welcome page
|   |-- stops.html               # commuter: live stops, problems table, pop-up
|   |-- demand.html              # drivers/associations: heat map
|   `-- report.html              # report form
`-- static/
    |-- style.css                # shared styles
    `-- taxis.jpg                # welcome page photo
```