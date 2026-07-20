import asyncio
import uuid

from search_agent import search_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from writer_agent import writer_agent, ReportData
from email_agent import email_agent


class ResearchManager:

    async def run(self, query: str):
        """
        Main Deep Research workflow.
        """

        trace_id = str(uuid.uuid4())

        yield f"🚀 Starting research...\n\nTrace ID: {trace_id}"

        search_plan = await self.plan_searches(query)

        yield f"🔎 Planned {len(search_plan.searches)} searches..."

        search_results = await self.perform_searches(search_plan)

        yield "📝 Writing report..."

        report = await self.write_report(query, search_results)

        yield "📧 Sending email..."

        await self.send_email(report)

        yield "✅ Research complete."

        yield report.markdown_report

    async def plan_searches(self, query: str) -> WebSearchPlan:
        """
        Ask the planner agent to generate a search plan.
        """
        return await planner_agent.run(query)

    async def perform_searches(
        self,
        search_plan: WebSearchPlan,
    ) -> list[str]:
        """
        Run all searches in parallel.
        """

        tasks = [
            self.search(item)
            for item in search_plan.searches
        ]

        return await asyncio.gather(*tasks)

    async def search(
        self,
        item: WebSearchItem,
    ) -> str:

        prompt = f"""
Search Term:
{item.query}

Reason:
{item.reason}
"""

        return await search_agent.run(prompt)

    async def write_report(
        self,
        query: str,
        search_results: list[str],
    ) -> ReportData:

        prompt = f"""
Original Research Question

{query}


Search Results

{search_results}
"""

        return await writer_agent.run(prompt)

    async def send_email(
        self,
        report: ReportData,
    ):

        await email_agent.run(report.markdown_report)