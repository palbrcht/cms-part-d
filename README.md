# cms-part-d

##  Purpose

Centers for Medicare & Medicaid Services (CMS) provide free and publicly available healthcare-related datasets pertaining to CMS expenditures and services.

One of those data sets reflects Medicare Part D drug utilization and expenditures.  In short, this data set shows what prescription drugs are being paid for by CMS for Medicare Part D beneficiaries.  This is an incredibly powerful resource for anyone interested in healthcare data.

I remember first analyzing this data during the Obama administration, which required you sometimes to download 50GB flat files directly to your computer.  However, this data is available via an API.

The purpose of this repository is to provide some guidance on how to use the CMS API to retrieve data you want.  I'll provide some basic functions and syntax.  I'd ultimately also like to make an API wrapper for Python and R.

This repo is moreso meant for researchers, health economists, data scientists, actuaries... really anyone who might not be super technical in a computer science sense but is curious about this data.

## What is Medicare and Medicare Part D?

The Centers for Medicare & Medicaid Services, CMS, is part of the Department of Health and Human Services (HHS). As the name implies, CMS runs Medicare, which is the United States federal health insurance program for:

* People who are 65 or older
* Certain younger people with disabilities
* People with End-Stage Renal Disease (permanent kidney failure requiring dialysis or a transplant, sometimes called ESRD)

Many people colloquially know Medicare as health insurance for the U.S. elderly.

Medicare provides different health plans which cover different parts of healthcare:

*  Medicare Part A (Hospital Insurance) - Part A covers inpatient hospital stays, care in a skilled nursing facility, hospice care, and some home health care.
*  Medicare Part B (Medical Insurance) - Part B covers certain doctors' services, outpatient care, medical supplies, and preventive services.
*  Medicare Part D (prescription drug coverage) - Helps cover the cost of prescription drugs (including many recommended shots or vaccines).

Check out more here: https://www.medicare.gov/what-medicare-covers/your-medicare-coverage-choices/whats-medicare

##  CMS Part D API

You can find the official Medicare Part D API documentation here: https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug/api-docs