# Eyabantu - Frontend Information

**BFB 321 Semester Project, Group 05 - Step 1: Frontend Build**

## Overview
We built the Eyabantu frontend as a mobile-first site using only HTML and CSS, without any JavaScript or external libraries. All four pages share one stylesheet and stick to a taxi-yellow and charcoal colour scheme. Because the backend database is only part of the final exam submission, the numbers shown on the site right now come from running our Python supply chain script (`run_eyabantu_demo.py`) across the six pilot routes into Pretoria CBD.

## Pages

| Page | File | Purpose |
|---|---|---|
| Welcome | `templates/index.html` | Introduces Eyabantu and sends commuters, drivers, and helpers to their specific page |
| Live stops | `templates/stops.html` | Shows commuters the next arriving taxis, rank problems, and the problem report pop-up |
| Demand heat map | `templates/demand.html` | Shows drivers and associations demand per stop, spare taxis to send, and recent reports |
| Report a stop or pickup | `templates/report.html` | Form where commuters log stops, confirm safe pickups, and rate how safe they felt |

Opening `index.html` in the main project folder redirects straight to the welcome page (`templates/index.html`).

### Welcome page (`templates/index.html`)
- Top banner with a minibus taxi photo and a brief intro to the project
- Yellow stats strip highlighting key figures from our proposal (15 million daily trips, 65-75% of public transport users, 6 pilot routes, and 7 taxi stops)
- Red SOS block that dials 10111 directly when tapped on a phone
- Three separate user cards (for commuters, drivers or associations, and general helpers) with buttons linking to their pages
- A short "How it works" breakdown alongside the list of six pilot routes and their stops

### Live stops (`templates/stops.html`)
- Next taxis table listing the stop name, route, ETA in minutes, and a Verified or Unverified status badge
- Numbered table of current problems at taxi ranks, ordered from the most reported issue down to the least
- A "Report a problem" pop-up window that opens and closes using pure CSS (`:target`) instead of JavaScript
- Three top KPI tiles showing expected waiting time, taxi occupancy percentage, and the count of verified stops

### Demand heat map (`templates/demand.html`)
- Demand table that translates raw passenger-to-seat ratios into plain labels (Very high, High, Moderate, Low) so drivers can read it at a glance
- Colour key above the table matching those four levels to dark red, light red, light orange, and light green rows
- Table showing the five newest submissions from the commuter report form
- Three KPI tiles at the top for spare taxis deployed, passengers waiting right now (740), and forecasted passengers for the next hour (776)

### Report a stop or pickup (`templates/report.html`)
- Dropdown menus to pick the stop, select one of the six Tshwane routes, and choose a report category, followed by a 1 to 5 safety score
- Three report options: "Taxi stops here", "I was picked up safely", and "I felt safe while waiting at this stop"

## Design Choices
We wrote the CSS for small phone screens first and used a `min-width: 760px` media query to expand the layout for tablets and laptops. To stop tables from overflowing sideways on phones, the Route and Taxis present columns hide automatically on narrow screens.

All four pages pull their styling from `static/style.css`, reusing the same code for the top bar, buttons, cards, tables, status badges, and KPI tiles. Users can click the Eyabantu logo at the top or the "Back to welcome page" button at the bottom of any screen to get back home. We also kept a single font family and a 16px spacing scale across the whole site so the pages look consistent.

## Accessibility and Form Validation
Every input box is paired with a proper HTML label, all tables use header tags, and the hero photo has descriptive alt text. Browser validation checks that required fields are filled in and keeps the safety rating strictly between 1 and 5. If someone enters an invalid value, a red error message shows up underneath that specific field to explain what needs fixing.

## Alignment with the Development Guide (Step 1)

| Requirement | How it is met |
|---|---|
| Responsive layout | Styled for mobile screens first and tested at 390px (phone) and 1280px (desktop) widths |
| Accessible forms and tables | Proper input labels, table headers, image alt text, and linked field error prompts |
| Client-side validation hints | Required attributes, number limits (1-5), input placeholders, and helper text |
| Reusable navbar, tables and cards | Shared component classes stored in a single `static/style.css` file |
| Table with route, ETA and status badges | Included in the Next taxis table on `stops.html` |
| Modal for updating exceptions | Built as a CSS-only "Report a problem" pop-up on `stops.html` |
| Mobile-friendly page for each main flow | Split into dedicated pages for commuters, drivers, and stop reporting |
| Form validation and helpful error messages | Field-specific red error prompts that only trigger on bad input |
| Consistent typography and spacing | One font family and a 16px spacing system across all four HTML files |

## Current Limitations
Because this step only covers the static frontend and standalone Python model, the pages display fixed demo numbers rather than live database queries. Clicking submit on the forms validates the inputs in the browser, but saving new reports requires the Flask API and MySQL database that we will connect for the final project submission. We also left out clickable column sorting on the tables since doing that properly requires JavaScript.