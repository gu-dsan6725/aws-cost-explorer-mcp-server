# AWS Cost Explorer MCP

A command-line interface and API for interacting with AWS Cost Explorer data through [Anthropic's MCP (Model Control Protocol)](https://www.anthropic.com/news/mcp).

## Overview

This tool provides a convenient way to analyze and visualize AWS cloud spending data using Anthropic's Claude model as an interactive interface. It functions as an MCP server that exposes AWS Cost Explorer API functionality to Claude, allowing you to ask questions about your AWS costs in natural language.

## Features

- **EC2 Spend Analysis**: View detailed breakdowns of EC2 spending for the last day
- **Service Spend Reports**: Analyze spending across all AWS services for the last 30 days
- **Detailed Cost Breakdown**: Get granular cost data by day, region, service, and instance type
- **Interactive Interface**: Use Claude to query your cost data through natural language

## Requirements

- Python 3.13+
- AWS credentials with Cost Explorer access
- Anthropic API access (for Claude integration)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/aarora79/aws-cost-explorer-mcp.git
   cd aws-cost-explorer-mcp
   ```

2. Install dependencies using UV (recommended) or pip:
   ```
   uv pip install --system -e .
   ```
   or
   ```
   pip install -e .
   ```

3. Configure your AWS credentials:
   ```
   mkdir -p ~/.aws
   # Set up your credentials in ~/.aws/credentials and ~/.aws/config
   ```

## Usage

### Starting the Server

Run the server using:

```
python server.py
```

By default, the server uses stdio transport for communication with MCP clients.

### Available Tools

The server exposes the following tools that Claude can use:

1. **get_ec2_spend_last_day()**: Retrieves EC2 spending data for the previous day
2. **get_service_spend_last_30_days()**: Provides a breakdown of spending by service over the last month
3. **get_detailed_breakdown_by_day(days=7)**: Delivers a comprehensive analysis of costs by region, service, and instance type

### Example Queries

Once connected to Claude through an MCP-enabled interface, you can ask questions like:

- "What was my EC2 spend yesterday?"
- "Show me my top 5 AWS services by cost for the last month"
- "Analyze my spending by region for the past 14 days"
- "Which instance types are costing me the most money?"

## Docker Support

A Dockerfile is included for containerized deployment:

```
docker build -t aws-cost-explorer-mcp .
docker run -v ~/.aws:/root/.aws aws-cost-explorer-mcp
```

## Development

### Project Structure

- `server.py`: Main server implementation with MCP tools
- `pyproject.toml`: Project dependencies and metadata
- `Dockerfile`: Container definition for deployments

### Adding New Cost Analysis Tools

To extend the functionality:

1. Add new functions to `server.py`
2. Annotate them with `@mcp.tool()`
3. Implement the AWS Cost Explorer API calls
4. Format the results for easy readability

## License

[MIT License](LICENSE)

## Acknowledgments

- This tool uses Anthropic's MCP framework
- Powered by AWS Cost Explorer API
- Built with FastMCP for server implementation