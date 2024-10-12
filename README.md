# IP Atlas

![IP Atlas Logo](link_to_your_logo) <!-- Change this if you want to add a logo -->

## Overview

IP Atlas is a project that includes two Python scripts designed to retrieve comprehensive information about IP addresses. It provides a user-friendly interface to easily obtain critical IP data essential for modern network analysis and security audits. The scripts gather detailed insights from both local and online sources, offering users robust analytical capabilities.

## Features

- **GeoIP2 Script**: Utilizes the GeoIP2 library to collect the following information:
  - **City**: Indicates the city associated with the IP address.
  - **Country**: Identifies the country of the IP address.
  - **Location Coordinates**: Provides latitude and longitude details, allowing users to pinpoint exact locations.
  - **ASN (Autonomous System Number)**: Contains organization information from the internet's routing system.

- **IPInfo Script**: Leverages the ipinfo.io API to provide similar insights:
  - **Organization Information**: Shows which organization the IP address belongs to.
  - **Abuse Reports**: Offers information on any history of abuse associated with the IP address, aiding in security analysis.

These scripts serve as powerful tools for network administrators, security experts, and curious users alike.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/glitchidea/IP-Atlas.git
   cd IP-Atlas
