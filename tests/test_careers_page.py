import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage
from pages.job_details_page import JobDetailsPage

def test_insider_careers_page(browser):
    home = HomePage(browser)
    careers = CareersPage(browser)
    qa_page = QAJobsPage(browser)
    job_details = JobDetailsPage(browser)

    # Step 1: Visit https://useinsider.com/ and check Insider home page is opened
    home.open_home_page("https://useinsider.com/")
    assert "Insider" in browser.title, "Insider home page not opened"

    # Step 2: Select Company > Careers and check careers page
    home.click_company_and_careers()
    assert "careers" in browser.current_url.lower(), "Careers page not opened"
    careers.verify_page_sections()

    # Step 3: Go to QA page and filter jobs
    qa_page.open_page("https://useinsider.com/careers/quality-assurance/")
    qa_page.click_see_all_jobs()
    qa_page.filter_jobs(location="Istanbul, Turkey", department="Quality Assurance")
    qa_page.wait_for_filter_to_complete()

    # Step 4: Check presence of the job list and verify details
    jobs = qa_page.verify_jobs_listed()
    qa_page.verify_jobs_details(jobs, position="Quality Assurance", department="Quality Assurance", location="Istanbul, Turkey" )

    # Step 5: Click "View Role" and verify redirect
    # Click on the first job's "View Role" button for demonstration
    qa_page.click_view_role()
    job_details.verify_lever_form_page()
