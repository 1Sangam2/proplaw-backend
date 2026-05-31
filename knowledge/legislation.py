"""
PropLaw AI — UK Property Law Knowledge Base
Real legislation text, structured for RAG retrieval.
Covers: Housing Acts, HMO, Deposits, Planning, Building Safety,
        Tenant Fees, Renters Reform, Leasehold, Safety Certs, and more.
"""

LEGISLATION_CHUNKS = [

    # ════════════════════════════════════════════════════════════════
    # ASSURED SHORTHOLD TENANCIES
    # ════════════════════════════════════════════════════════════════
    {
        "id": "ha88_ast",
        "source": "Housing Act 1988 (as amended by Housing Act 1996)",
        "citation": "Housing Act 1988, s.19A; Housing Act 1996, s.96",
        "category": "Tenancy Types",
        "title": "Assured Shorthold Tenancy — Definition & Default Status",
        "text": (
            "An Assured Shorthold Tenancy (AST) is the default form of private residential "
            "tenancy in England and Wales. Since 28 February 1997, all new private tenancies "
            "automatically become ASTs unless the parties specifically contract otherwise in "
            "writing. An AST requires: (1) the tenant is an individual; (2) the property is "
            "the tenant's only or principal home; (3) annual rent is between £1,000 and "
            "£100,000. Fixed-term ASTs must run for a minimum of 6 months — courts cannot "
            "grant possession during the first 6 months regardless of grounds. After the "
            "fixed term expires, the tenancy becomes a statutory periodic tenancy (rolling "
            "month-to-month) unless a new fixed term is expressly agreed. Tenancies excluded "
            "from AST status include: resident landlord situations, company lets, holiday "
            "lets, and properties with annual rent exceeding £100,000."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # SECTION 21 — NO-FAULT EVICTION
    # ════════════════════════════════════════════════════════════════
    {
        "id": "ha88_s21_core",
        "source": "Housing Act 1988, Section 21",
        "citation": "Housing Act 1988, s.21; Deregulation Act 2015, s.33-41",
        "category": "Eviction — Section 21",
        "title": "Section 21 Notice — Requirements, Validity & Process",
        "text": (
            "Section 21 of the Housing Act 1988 permits a landlord to recover possession of "
            "an AST property without proving fault ('no-fault eviction'). For tenancies "
            "granted on or after 1 October 2015, landlords must use Form 6A. Key validity "
            "requirements — a Section 21 notice is INVALID if any of the following apply: "
            "(1) Deposit not protected in an approved TDP scheme within 30 days of receipt; "
            "(2) Prescribed deposit information not provided to the tenant; "
            "(3) Valid Gas Safety Certificate not provided before occupation; "
            "(4) Current Electrical Installation Condition Report (EICR) not provided; "
            "(5) Valid Energy Performance Certificate (EPC) not provided; "
            "(6) Government 'How to Rent' guide not provided (correct version at tenancy start); "
            "(7) Property is an unlicensed HMO or in a selective licensing area without licence; "
            "(8) Local authority has served an Improvement Notice within the preceding 6 months; "
            "(9) Notice served within first 4 months of tenancy. "
            "Notice period: minimum 2 months. The notice expires 6 months from date of service — "
            "court proceedings must commence within 6 months. Accelerated possession procedure "
            "available if no rent arrears and no disrepair counterclaim."
        ),
    },
    {
        "id": "ha88_s21_abolition",
        "source": "Renters' Rights Act 2025",
        "citation": "Renters' Rights Act 2025",
        "category": "Eviction — Section 21",
        "title": "Section 21 Abolition — Renters' Rights Act 2025",
        "text": (
            "The Renters' Rights Act 2025 abolishes Section 21 no-fault evictions entirely. "
            "This is the most fundamental change to English tenancy law in over 30 years. "
            "From commencement: no new Section 21 notices can be served; all existing "
            "tenancies (including those already periodic) will convert to the new system. "
            "Landlords will only be able to regain possession using expanded Section 8 "
            "grounds. New mandatory grounds introduced include: Ground 1A — landlord wishes "
            "to sell the property (2 months' notice, cannot be used within first 12 months "
            "of tenancy); Ground 1B — landlord or close family member wishes to move in "
            "(2 months' notice, cannot be used within first 12 months). "
            "Tenants gain the right to end any tenancy by giving 2 months' notice at any time. "
            "Fixed-term ASTs are abolished for new tenancies — all tenancies will be periodic "
            "from the outset."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # SECTION 8 — FAULT-BASED EVICTION
    # ════════════════════════════════════════════════════════════════
    {
        "id": "ha88_s8",
        "source": "Housing Act 1988, Section 8 & Schedule 2",
        "citation": "Housing Act 1988, s.8; Schedule 2 (as amended)",
        "category": "Eviction — Section 8",
        "title": "Section 8 — Grounds for Possession & Notice Periods",
        "text": (
            "Section 8 of the Housing Act 1988 permits possession where specific grounds in "
            "Schedule 2 are established. A Notice Seeking Possession (Form 3) must be served "
            "before court proceedings. Key grounds: "
            "MANDATORY GROUNDS (court must grant if proved): "
            "Ground 8 — At least 2 months' rent in arrears both at date of notice AND at "
            "hearing (2 weeks' notice required); "
            "Ground 1 — Landlord previously occupied as only/principal home (2 months' notice); "
            "Ground 2 — Mortgage lender seeking possession (2 months' notice); "
            "Ground 7A — Domestic violence (2–4 weeks' notice). "
            "DISCRETIONARY GROUNDS (court may grant if reasonable): "
            "Ground 10 — Some rent arrears at notice and hearing (2 weeks' notice); "
            "Ground 11 — Persistent late payment even if not in arrears (2 weeks' notice); "
            "Ground 12 — Breach of tenancy obligation (2 weeks' notice); "
            "Ground 13 — Deterioration of property (2 weeks' notice); "
            "Ground 14 — Nuisance, annoyance, or conviction for illegal/immoral use — "
            "IMMEDIATE notice, proceedings can start day after service; "
            "Ground 17 — Tenant induced landlord to grant tenancy by false statement (2 weeks)."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # HMO — DEFINITION & LICENSING
    # ════════════════════════════════════════════════════════════════
    {
        "id": "ha04_hmo_def",
        "source": "Housing Act 2004, Section 254",
        "citation": "Housing Act 2004, s.254-259",
        "category": "HMO — Definition",
        "title": "HMO Definition — What Constitutes a House in Multiple Occupation",
        "text": (
            "Under Section 254 of the Housing Act 2004, a House in Multiple Occupation (HMO) "
            "is a building or part of a building that: (a) is occupied by more than one "
            "household; and (b) at least two of the households share, or lack, an amenity "
            "such as a bathroom, toilet, or cooking facilities. A 'household' means a family "
            "unit: a single person, a married or cohabiting couple (including same-sex), or "
            "a family (parents/grandparents and children/grandchildren, including step and "
            "foster relationships). Key HMO types: (1) Shared houses — 3+ unrelated people "
            "sharing kitchen/bathroom; (2) Bedsit properties — self-contained rooms with "
            "shared facilities; (3) Converted buildings where not all flats are self-contained "
            "(Section 257 HMOs). A property with only 2 people from 2 households sharing is "
            "NOT an HMO. Purpose-built student accommodation managed by universities, "
            "buildings regulated under other legislation (care homes, bail hostels), and "
            "owner-occupied properties with 2 or fewer lodgers are generally exempt."
        ),
    },
    {
        "id": "ha04_hmo_mandatory_lic",
        "source": "Housing Act 2004 / HMO Licensing Regulations 2018",
        "citation": "Housing Act 2004, s.55-78; SI 2018/221",
        "category": "HMO — Licensing",
        "title": "Mandatory HMO Licensing — Threshold, Application & Penalties",
        "text": (
            "Since 1 October 2018 (SI 2018/221), mandatory HMO licensing applies to ALL HMOs "
            "in England occupied by 5 or more people forming 2 or more separate households, "
            "regardless of the number of storeys (previously only 3+ storey HMOs were covered). "
            "Licence applications must be made to the local housing authority before the HMO "
            "is occupied. Licence duration: up to 5 years. Conditions attached to every licence "
            "include: minimum room size requirements; maximum number of permitted occupants; "
            "fire safety standards; gas and electrical safety certificate obligations. "
            "Mandatory room size standards (SI 2018/234): sleeping room used by one person "
            "aged 10 or over — minimum 6.51 sq metres; room used by two persons aged 10 or "
            "over — minimum 10.22 sq metres; room used by a child under 10 — minimum 4.64 sq "
            "metres. Rooms below these sizes must not be used as sleeping accommodation. "
            "Operating an unlicensed HMO is a criminal offence: unlimited fine on conviction. "
            "Local authorities may also impose civil financial penalties of up to £30,000 per "
            "breach. Tenants in an unlicensed HMO can apply to the First-tier Tribunal for a "
            "Rent Repayment Order (RRO) covering up to 12 months' rent."
        ),
    },
    {
        "id": "ha04_hmo_additional",
        "source": "Housing Act 2004, Part 2",
        "citation": "Housing Act 2004, s.56; Housing Act 2004, s.80",
        "category": "HMO — Licensing",
        "title": "Additional & Selective Licensing Schemes",
        "text": (
            "Beyond mandatory licensing, local authorities have two further licensing powers: "
            "ADDITIONAL LICENSING (s.56 HA 2004): Councils can extend HMO licensing to cover "
            "smaller HMOs (e.g. 3 or 4 occupiers) in their area if satisfied that a "
            "significant proportion of HMOs are being managed sufficiently ineffectively. "
            "No Government approval required for schemes covering less than 20% of the area. "
            "SELECTIVE LICENSING (s.80 HA 2004): Councils can require ALL privately rented "
            "properties (not just HMOs) in a designated area to be licensed, where the area "
            "has: low housing demand; significant anti-social behaviour; high deprivation; "
            "high crime levels; or poor property conditions. "
            "Schemes covering more than 20% of the council's area, or more than 20% of "
            "private rented housing, require Secretary of State approval. "
            "Licence fees vary by council (typically £200–£900 per property). "
            "Failure to licence in a selective licensing area: criminal offence, unlimited fine, "
            "and tenants can apply for a Rent Repayment Order."
        ),
    },
    {
        "id": "ha04_hmo_management_regs",
        "source": "The Management of Houses in Multiple Occupation (England) Regulations 2006",
        "citation": "SI 2006/372",
        "category": "HMO — Management",
        "title": "HMO Management Regulations — Manager's Legal Duties",
        "text": (
            "The Management of HMOs (England) Regulations 2006 (SI 2006/372) impose specific "
            "ongoing duties on HMO managers (the person having control/managing the property). "
            "The manager MUST: (1) Display their name, address and telephone number in a "
            "prominent position in the HMO; (2) Ensure all means of escape from fire are kept "
            "free from obstruction, maintained in good repair, and in good order at all times; "
            "(3) Ensure all fire-fighting equipment and fire alarms are maintained in proper "
            "working order; (4) Ensure all common parts (hallways, staircases, landings, "
            "bathrooms, WCs) are maintained in good repair, clean condition, and adequate "
            "decorative order; (5) Ensure adequate lighting is provided and maintained in all "
            "common parts; (6) Ensure water supply and drainage systems are maintained; "
            "(7) Ensure electrical installations are maintained in good repair and safe condition; "
            "(8) Ensure adequate facilities for the disposal of refuse are provided; "
            "(9) Take reasonable steps to ensure that the conduct of occupants does not "
            "adversely affect persons occupying other parts of the building or neighbours. "
            "Breach of these regulations is a criminal offence — local authorities can "
            "prosecute or issue civil penalty notices up to £30,000."
        ),
    },
    {
        "id": "hmo_fire_safety",
        "source": "Regulatory Reform (Fire Safety) Order 2005 / Housing Act 2004",
        "citation": "SI 2005/1541; Housing Act 2004, Schedule 1 (HHSRS)",
        "category": "HMO — Fire Safety",
        "title": "HMO Fire Safety — Required Measures by Size",
        "text": (
            "HMO fire safety requirements scale with the size and type of property. "
            "ALL HMOs require: interlinked smoke alarms on every floor; heat detector in "
            "kitchen; carbon monoxide detector where solid fuel appliances are present; "
            "fire blanket in kitchen area. "
            "LARGER HMOs (typically 3+ storeys or 5+ occupants) additionally require: "
            "mains-wired interlinked smoke/heat detection system; fire doors (FD30 minimum) "
            "to all habitable rooms on escape routes; intumescent strips and cold smoke seals "
            "to fire doors; thumb-turn locks (not key-operated) on all exit doors; emergency "
            "escape lighting in common areas; Fire Risk Assessment (required under the "
            "Regulatory Reform (Fire Safety) Order 2005 for common parts). "
            "The Regulatory Reform (Fire Safety) Order 2005 applies to the common parts of "
            "HMOs — the 'responsible person' (usually the landlord/manager) must carry out "
            "and regularly review a Fire Risk Assessment. "
            "The Housing Health and Safety Rating System (HHSRS) under Schedule 1 of the "
            "Housing Act 2004 assesses fire risk as a Category 1 hazard — councils are "
            "legally required to take enforcement action where Category 1 hazards exist."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # DEPOSIT PROTECTION
    # ════════════════════════════════════════════════════════════════
    {
        "id": "ha04_deposit",
        "source": "Housing Act 2004, ss.212-215 / Localism Act 2011",
        "citation": "Housing Act 2004, s.212-215; Localism Act 2011, s.184-186",
        "category": "Deposit Protection",
        "title": "Tenancy Deposit Protection — Full Legal Requirements",
        "text": (
            "Since 6 April 2007, landlords must protect all tenancy deposits in an approved "
            "Tenancy Deposit Protection (TDP) scheme within 30 days of receipt. The three "
            "Government-approved schemes are: Deposit Protection Service (DPS) — custodial "
            "and insured options; MyDeposits — insured; Tenancy Deposit Scheme (TDS) — "
            "custodial and insured. Landlords must also provide 'Prescribed Information' "
            "to the tenant within 30 days, covering: the deposit amount; the TDP scheme "
            "details; how to apply for repayment; what to do in a dispute; the circumstances "
            "under which deductions may be made. "
            "PENALTIES for non-compliance (s.214 HA 2004 as amended by Localism Act 2011): "
            "(1) Court must order deposit to be repaid or protected within 14 days; "
            "(2) Court must order landlord to pay tenant a penalty of between 1x and 3x the "
            "deposit amount — at court's discretion based on degree of non-compliance; "
            "(3) Landlord cannot serve a valid Section 21 notice until the deposit is protected "
            "and prescribed information served, or the deposit is returned in full. "
            "The deposit cap (Tenant Fees Act 2019): 5 weeks' rent (annual rent under £50,000); "
            "6 weeks' rent (annual rent £50,000 or over). "
            "Disputes: free ADR service provided by the TDP scheme — adjudicator's decision "
            "is binding. Deposit must be returned within 10 days of an agreed claim."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # TENANT FEES ACT 2019
    # ════════════════════════════════════════════════════════════════
    {
        "id": "tfa19",
        "source": "Tenant Fees Act 2019",
        "citation": "Tenant Fees Act 2019 (c.4)",
        "category": "Tenant Fees",
        "title": "Tenant Fees Act 2019 — Prohibited Payments & Permitted Charges",
        "text": (
            "The Tenant Fees Act 2019 (in force 1 June 2019) bans landlords and letting agents "
            "from charging tenants any fee not expressly permitted by the Act. "
            "PROHIBITED payments include: administration fees; referencing fees; credit check "
            "fees; guarantor arrangement fees; inventory fees; check-in/check-out fees; fees "
            "for viewing properties; renewal or extension fees; fees for permitted alterations "
            "to the tenancy agreement at the landlord's request. "
            "PERMITTED payments are strictly limited to: (1) Rent; (2) Refundable tenancy "
            "deposit — capped at 5 weeks' rent (under £50k pa) or 6 weeks' (£50k+ pa); "
            "(3) Refundable holding deposit — capped at 1 week's rent, must be repaid within "
            "15 days; (4) Default payments — late payment charge capped at 3% above Bank of "
            "England base rate on outstanding rent (after 14 days overdue); reasonable "
            "key/security device replacement costs with evidence; (5) Tenant-requested "
            "changes — capped at £50 or reasonable costs if higher; (6) Early termination "
            "requested by tenant — landlord's genuine financial loss only. "
            "PENALTIES: first breach — financial penalty up to £5,000; second breach within "
            "5 years — criminal offence with unlimited fine and banning order risk. "
            "Any prohibited payment received is a 'relevant offence' preventing a valid "
            "Section 21 notice until the payment is repaid."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # LANDLORD REPAIRS
    # ════════════════════════════════════════════════════════════════
    {
        "id": "lta85_s11",
        "source": "Landlord and Tenant Act 1985, Sections 11-16",
        "citation": "Landlord and Tenant Act 1985, s.11-16",
        "category": "Repairs & Maintenance",
        "title": "Section 11 LTA 1985 — Implied Repairing Covenants",
        "text": (
            "Section 11 of the Landlord and Tenant Act 1985 implies repairing obligations "
            "into all residential tenancies of less than 7 years' duration (including all "
            "ASTs). The landlord is obligated to keep in repair and proper working order: "
            "(1) The structure and exterior of the dwelling — including roof, walls, windows, "
            "external doors, drains, gutters, and external pipes; (2) Installations for the "
            "supply of water, gas, electricity and sanitation — including basins, sinks, baths, "
            "showers and sanitary conveniences; (3) Installations for space heating and water "
            "heating — including boilers, radiators, immersion heaters, and associated pipework. "
            "The standard of repair required is that appropriate for the age, character and "
            "locality of the property. The landlord is NOT liable for: repairs caused by the "
            "tenant's misuse or negligence; internal decorative order; tenant's own fixtures "
            "and fittings. CRITICAL: the landlord must be given notice of a defect before "
            "they can be in breach — the obligation to repair arises only after the landlord "
            "has actual knowledge of the problem. Once notified, repairs must be carried out "
            "within a reasonable time — urgency determines what is 'reasonable' (a broken "
            "boiler in winter requires faster action than a cracked ceiling)."
        ),
    },
    {
        "id": "hfhha18",
        "source": "Homes (Fitness for Human Habitation) Act 2018",
        "citation": "Homes (Fitness for Human Habitation) Act 2018 (c.34)",
        "category": "Repairs & Maintenance",
        "title": "Fitness for Human Habitation — Tenant's Right of Action",
        "text": (
            "The Homes (Fitness for Human Habitation) Act 2018 amends the Landlord and Tenant "
            "Act 1985 to require that all rented residential property in England must be fit "
            "for human habitation at the beginning of the tenancy and throughout. Applies to "
            "all tenancies — there is no minimum term requirement. Relevant matters indicating "
            "unfitness include: serious disrepair; structural instability; dampness prejudicial "
            "to health; inadequate natural lighting or ventilation; inadequate water or "
            "drainage facilities; lack of adequate facilities for preparation/cooking of food; "
            "any hazard within the meaning of the Housing Act 2004 (including HHSRS Category 1 "
            "and 2 hazards). Damp and mould is explicitly covered — a property with damp or "
            "mould affecting the health of occupants will typically be deemed unfit. "
            "REMEDY: Tenants can bring civil proceedings in the County Court for: damages "
            "(compensation for harm suffered including health impacts, damage to possessions, "
            "inconvenience); AND/OR an injunction compelling the landlord to carry out works. "
            "Unlike Section 11, a tenant can bring an action even if the landlord has no "
            "formal notice of the defect, if the landlord reasonably ought to have known."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # SAFETY CERTIFICATES
    # ════════════════════════════════════════════════════════════════
    {
        "id": "gas_safety_regs",
        "source": "Gas Safety (Installation and Use) Regulations 1998",
        "citation": "SI 1998/2451, Regulation 36",
        "category": "Safety Certificates",
        "title": "Gas Safety Certificate (CP12) — Annual Landlord Obligations",
        "text": (
            "Regulation 36 of the Gas Safety (Installation and Use) Regulations 1998 requires "
            "landlords of residential properties containing gas appliances to: "
            "(1) Arrange an annual gas safety check by a Gas Safe registered engineer on all "
            "gas appliances, flues, and associated pipework; (2) Obtain a Gas Safety Record "
            "(also called a CP12 certificate) — the record must include: the date of inspection; "
            "the address; the engineer's Gas Safe registration number; each appliance checked; "
            "any defects identified; the engineer's signature. "
            "(3) Provide a copy of the Gas Safety Record to: existing tenants within 28 days "
            "of the check; new tenants before they occupy the property. "
            "(4) Retain records of all gas safety checks for a minimum of 2 years. "
            "A new tenant must be provided with the most recent certificate before move-in. "
            "ENFORCEMENT: failure to comply is a criminal offence — prosecution can result in "
            "an unlimited fine and/or up to 6 months' imprisonment. A Section 21 notice is "
            "rendered invalid if the gas safety certificate was not provided to the tenant "
            "before the tenancy commenced (Deregulation Act 2015, s.41)."
        ),
    },
    {
        "id": "electrical_safety",
        "source": "Electrical Safety Standards in the Private Rented Sector (England) Regulations 2020",
        "citation": "SI 2020/312",
        "category": "Safety Certificates",
        "title": "EICR — Electrical Safety Inspection Requirements",
        "text": (
            "The Electrical Safety Standards in the Private Rented Sector (England) Regulations "
            "2020 (SI 2020/312) require landlords to: (1) Ensure electrical installations are "
            "inspected and tested at intervals not exceeding 5 years by a qualified and "
            "competent person; (2) Obtain an Electrical Installation Condition Report (EICR) "
            "following inspection; (3) Supply a copy of the EICR to: existing tenants within "
            "28 days of inspection; new tenants before they occupy; prospective tenants within "
            "28 days of request; local housing authority within 7 days of request. "
            "(4) Where the EICR identifies: a C1 (Danger present — risk of injury) or C2 "
            "(Potentially dangerous) finding — landlord must carry out the remedial work and "
            "obtain written confirmation from an electrician within 28 days of the EICR "
            "(or within the period specified in the report if shorter); FI (Further Investigation "
            "required) — investigation must be completed within 28 days. "
            "PENALTIES: local authorities can impose financial penalties of up to £30,000 "
            "per breach. Applies to all new tenancies from 1 July 2020 and all existing "
            "tenancies from 1 April 2021."
        ),
    },
    {
        "id": "epc_mees",
        "source": "Energy Performance of Buildings Regulations 2012 / MEES Regulations 2015",
        "citation": "SI 2012/3118; SI 2015/962 (as amended by SI 2019/595)",
        "category": "Safety Certificates",
        "title": "EPC & Minimum Energy Efficiency Standards (MEES)",
        "text": (
            "Landlords must obtain and provide a valid Energy Performance Certificate (EPC) "
            "to prospective tenants before marketing a property for rent. An EPC rates a "
            "property A (most efficient) to G (least efficient) and is valid for 10 years. "
            "MINIMUM ENERGY EFFICIENCY STANDARDS (MEES) — Energy Efficiency (Private Rented "
            "Property) (England and Wales) Regulations 2015 (SI 2015/962): Since 1 April 2020, "
            "it has been unlawful to grant a new tenancy for any property rated F or G. "
            "Since 1 April 2023, all privately rented properties (including existing tenancies) "
            "must be rated E or above — F and G rated properties cannot be rented even if "
            "no new tenancy is being granted. PROPOSED FUTURE STANDARD: The Government has "
            "proposed raising the minimum to EPC C by 2028 for new tenancies and 2030 for "
            "all tenancies (not yet law as of 2025). EXEMPTIONS: landlords can register an "
            "exemption on the PRS Exemptions Register where: all relevant energy efficiency "
            "improvements have been made but the property remains below E; cost of improvements "
            "exceeds the £3,500 cost cap; third-party consent cannot be obtained (e.g. planning "
            "or listed building consent). PENALTIES: up to £5,000 per property for breach. "
            "An invalid EPC also renders a Section 21 notice invalid."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # RENTERS RIGHTS ACT 2025
    # ════════════════════════════════════════════════════════════════
    {
        "id": "rra2025",
        "source": "Renters' Rights Act 2025",
        "citation": "Renters' Rights Act 2025",
        "category": "Renters Reform",
        "title": "Renters' Rights Act 2025 — Comprehensive Overview",
        "text": (
            "The Renters' Rights Act 2025 is the most significant reform to the private rented "
            "sector in England since the Housing Act 1988. Key provisions: "
            "ABOLITION OF SECTION 21: no-fault evictions ended entirely — landlords must rely "
            "on expanded Section 8 grounds. "
            "TENANCY STRUCTURE: all tenancies will be periodic (rolling) from the outset — "
            "fixed-term ASTs abolished for new tenancies; existing fixed terms will run to "
            "expiry then convert to periodic. "
            "TENANT NOTICE: tenants can end any periodic tenancy by giving 2 months' notice "
            "at any point — no minimum term for the tenant. "
            "RENT INCREASES: landlords may only increase rent once per year using the Section "
            "13 procedure; tenants can challenge above-market increases at the First-tier "
            "Tribunal; in-tenancy rent increase clauses in existing agreements are overridden. "
            "DECENT HOMES STANDARD: for the first time, the Decent Homes Standard will be "
            "applied to the private rented sector — enforcement through local authorities. "
            "OMBUDSMAN: all private landlords must join a new mandatory PRS Ombudsman scheme. "
            "LANDLORD PORTAL: all landlords must register on a new Property Portal (Landlord "
            "Database) — operating without registration will be a criminal offence. "
            "DISCRIMINATION: blanket bans on renting to families with children (under 18) or "
            "tenants receiving benefits will be unlawful. "
            "PETS: landlords must consider pet requests and cannot unreasonably refuse — "
            "they can require pet insurance."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # BUILDING SAFETY ACT 2022
    # ════════════════════════════════════════════════════════════════
    {
        "id": "bsa22_hrb",
        "source": "Building Safety Act 2022",
        "citation": "Building Safety Act 2022 (c.30), Parts 2-4",
        "category": "Building Safety",
        "title": "Building Safety Act 2022 — Higher-Risk Buildings Regime",
        "text": (
            "The Building Safety Act 2022 introduced a new regulatory framework for building "
            "safety following the Grenfell Tower fire (2017). "
            "HIGHER-RISK BUILDINGS (HRBs): defined as buildings that are at least 18 metres "
            "in height or have at least 7 storeys, AND contain at least 2 residential units. "
            "REGISTRATION: all HRBs must be registered with the Building Safety Regulator "
            "(BSR, operated by the Health and Safety Executive). Occupation of an unregistered "
            "HRB became a criminal offence from April 2024. "
            "ACCOUNTABLE PERSON: every HRB must have a named Principal Accountable Person "
            "(the entity responsible for the exterior/structure — typically the freeholder or "
            "head leaseholder) and may have additional Accountable Persons for different parts. "
            "BUILDING SAFETY CASE: a Safety Case Report must be produced and submitted to the "
            "BSR, demonstrating how building safety risks are being managed on an ongoing basis. "
            "BSR has powers to: issue compliance notices; impose improvement notices; restrict "
            "occupation of unsafe buildings. "
            "EXTENDED LIMITATION PERIODS: residents can pursue developers/builders for latent "
            "building defects for up to 30 years (retrospective) — significantly extending "
            "the previous 6-year limitation period."
        ),
    },
    {
        "id": "bsa22_leaseholder",
        "source": "Building Safety Act 2022, Part 5",
        "citation": "Building Safety Act 2022, s.116-125; Schedule 8",
        "category": "Building Safety",
        "title": "Leaseholder Protections — Cladding & Remediation Cost Caps",
        "text": (
            "Part 5 and Schedule 8 of the Building Safety Act 2022 introduced landmark "
            "protections for leaseholders against being charged for building safety remediation. "
            "QUALIFYING LEASEHOLDERS: a leaseholder who, on 14 February 2022, owned the "
            "leasehold of a residential unit in an affected building — whether or not they "
            "were living there. "
            "ABSOLUTE PROTECTIONS — qualifying leaseholders CANNOT be charged for: "
            "cladding remediation costs — in all circumstances, regardless of the nature of "
            "the cladding or the building's height; any remediation costs where the landlord, "
            "developer, or associated company was responsible for creating the defect. "
            "COST CAPS — for other non-cladding remediation: maximum chargeable is £15,000 "
            "(Greater London) or £10,000 (elsewhere) over a 5-year period per leaseholder. "
            "Buildings below 11 metres: qualifying leaseholders are fully protected from all "
            "relevant defect costs. "
            "ENFORCEMENT: service charge demands that breach these protections are unenforceable. "
            "Leaseholders may apply to the First-tier Tribunal (Property Chamber) to challenge "
            "unlawful demands. Landlords who continue to demand unlawful service charges face "
            "civil penalties."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # PLANNING LAW
    # ════════════════════════════════════════════════════════════════
    {
        "id": "planning_pd",
        "source": "Town and Country Planning (GPDO) (England) Order 2015",
        "citation": "SI 2015/596 (as amended)",
        "category": "Planning",
        "title": "Permitted Development Rights — Residential Extensions & Conversions",
        "text": (
            "The Town and Country Planning (General Permitted Development) (England) Order 2015 "
            "(SI 2015/596) grants automatic planning permission (Permitted Development / PD) "
            "for certain types of development without a full planning application. "
            "RESIDENTIAL EXTENSIONS: single-storey rear extensions up to 6m for terraced/"
            "semi-detached houses and 8m for detached houses (subject to neighbour consultation); "
            "maximum height 4m; must not exceed 50% of curtilage. Two-storey rear extensions: "
            "no more than 3m beyond the original rear wall. Loft conversions: up to 40 cubic "
            "metres of additional roof space for terraced houses; 50 cubic metres for detached "
            "and semi-detached. OUTBUILDINGS: total area not to exceed 50% of the garden; "
            "max 4m ridge height (2.5m within 2m of boundary). "
            "CHANGE OF USE — Class MA: conversion of commercial/retail/leisure premises (Class E) "
            "to residential (Class C3) — prior approval required from local authority. "
            "IMPORTANT RESTRICTIONS: PD rights do not apply to: listed buildings; "
            "land in a Conservation Area (some restrictions); Article 4 Direction areas "
            "(where council has removed PD rights — common in HMO-dense or conservation areas); "
            "flats and maisonettes (most extensions/conversions require full planning permission). "
            "Always verify PD rights with the local planning authority before commencing works."
        ),
    },
    {
        "id": "planning_hmo_c4",
        "source": "Town and Country Planning (Use Classes) Order 1987 (as amended)",
        "citation": "SI 1987/764 (as amended by SI 2010/653)",
        "category": "Planning",
        "title": "HMO Planning — Use Classes C3/C4 & Article 4 Directions",
        "text": (
            "The Use Classes Order is critical for HMO developers and agents. "
            "CLASS C3 (Dwellinghouses): covers a property occupied by a single person, a "
            "couple, or a family — and by up to 6 people living together as a single household. "
            "CLASS C4 (Houses in Multiple Occupation): covers small HMOs with 3 to 6 unrelated "
            "occupants sharing facilities. Change of use from C3 to C4 is normally Permitted "
            "Development (no planning application required). "
            "LARGE HMOs (7+ occupants): classified as Sui Generis — always requires full "
            "planning permission regardless of Article 4 Directions. "
            "ARTICLE 4 DIRECTIONS: many councils have made Article 4 Directions removing the "
            "C3-to-C4 PD right in designated areas (typically high-density rental areas, "
            "university towns). Where an Article 4 Direction applies: planning permission IS "
            "required before converting a C3 property to an HMO. Operating a C4 HMO without "
            "permission in an Article 4 area is a planning breach — subject to enforcement "
            "action including a planning enforcement notice and injunction. "
            "Councils are required to publish Article 4 Direction maps — always check the "
            "local planning authority's website and interactive planning map before conversion."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # RIGHT TO RENT
    # ════════════════════════════════════════════════════════════════
    {
        "id": "right_to_rent",
        "source": "Immigration Act 2014, Part 3",
        "citation": "Immigration Act 2014, s.20-37 (as amended by Immigration Act 2016)",
        "category": "Right to Rent",
        "title": "Right to Rent — Landlord Checks & Penalties",
        "text": (
            "The Immigration Act 2014 (in force in England from 1 February 2016) requires "
            "landlords to verify that all adult occupants (aged 18+) have the legal right to "
            "rent in the UK before a tenancy commences. Right to rent checks apply to ALL "
            "occupants — not just the named tenant. "
            "ACCEPTABLE DOCUMENTS: UK/Irish passports; Biometric Residence Permits; "
            "Settled/Pre-Settled Status (checked via Home Office online share code service at "
            "gov.uk/view-right-to-rent); other acceptable List A or List B documents. "
            "PROCESS: (1) Request original documents; (2) Check validity in the tenant's "
            "presence; (3) Copy and retain documents; (4) Record the date of the check. "
            "TIME-LIMITED RIGHT TO RENT: where a tenant has time-limited leave (e.g. work visa), "
            "landlords must carry out repeat checks at the earlier of: 12 months from initial "
            "check, or the expiry of the leave. "
            "PENALTIES (significantly increased by the Illegal Migration Act 2023): "
            "Civil penalty: up to £5,000 per lodger / £10,000 per occupant for a first breach; "
            "up to £10,000 per lodger / £20,000 per occupant for repeat breaches. "
            "Criminal offence: knowingly renting to a person with no right to rent — "
            "unlimited fine and/or up to 5 years' imprisonment."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # LANDLORD ACCESS & HARASSMENT
    # ════════════════════════════════════════════════════════════════
    {
        "id": "landlord_access_harassment",
        "source": "Landlord and Tenant Act 1985 / Protection from Eviction Act 1977",
        "citation": "LTA 1985, s.11; Protection from Eviction Act 1977, s.1-2",
        "category": "Landlord Access & Harassment",
        "title": "Right to Access, Quiet Enjoyment & Harassment Law",
        "text": (
            "LANDLORD ACCESS: A landlord has an implied right to enter the property to inspect "
            "its condition and carry out repairs — but MUST give the tenant at least 24 hours' "
            "prior written notice and may only enter at reasonable times of the day. This right "
            "arises from Section 11 of the LTA 1985 and is typically reflected in the tenancy "
            "agreement. Entry without notice, or without the tenant's consent despite notice, "
            "is a trespass and potentially a criminal offence. "
            "QUIET ENJOYMENT: every residential tenancy contains an implied covenant of quiet "
            "enjoyment — the landlord must not substantially interfere with the tenant's right "
            "to use and enjoy the property. Repeated unannounced visits, removing or withholding "
            "services, or interfering with the property can breach this covenant — actionable "
            "in civil proceedings for damages and/or injunction. "
            "HARASSMENT (Protection from Eviction Act 1977, s.1): It is a criminal offence "
            "for a landlord (or their agent) to do acts calculated to interfere with the "
            "peace/comfort of a residential occupier, or to persistently withdraw/withhold "
            "services reasonably required for occupation, with intent to cause the occupier "
            "to give up occupation or refrain from exercising legal rights. "
            "ILLEGAL EVICTION (s.1(2) PEA 1977): unlawfully depriving a residential occupier "
            "of occupation, or attempting to do so, is a criminal offence — unlimited fine "
            "and/or up to 2 years' imprisonment."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # RENT INCREASES
    # ════════════════════════════════════════════════════════════════
    {
        "id": "rent_increase",
        "source": "Housing Act 1988, Section 13",
        "citation": "Housing Act 1988, s.13-14",
        "category": "Rent",
        "title": "Rent Increases — Section 13 Procedure & Tribunal Challenge",
        "text": (
            "For periodic Assured Shorthold Tenancies, a landlord can only increase the rent "
            "lawfully via one of two routes: (1) A rent review clause in the tenancy agreement "
            "(which must set out precisely how and when rent may increase); or (2) The Section "
            "13 statutory procedure using Form 4 (Landlord's Notice Proposing a New Rent). "
            "SECTION 13 REQUIREMENTS: the notice must state the proposed new rent and the date "
            "from which it is to take effect. Minimum notice period: for a monthly periodic "
            "tenancy — 1 month's notice; for a quarterly tenancy — 3 months' notice; for a "
            "yearly tenancy — 6 months' notice. The new rent can only take effect on the "
            "anniversary of the tenancy start date (first rent date for periodic tenancies). "
            "TENANT CHALLENGE: the tenant may refer the notice to the First-tier Tribunal "
            "(Property Chamber) before the proposed effective date — the Tribunal will "
            "determine the open market rent and set that as the new rent. "
            "RENTERS' RIGHTS ACT 2025 REFORM: rent increases limited to once per year via "
            "Section 13 procedure only; in-tenancy contractual rent escalation clauses are "
            "overridden; above-market increases can be challenged at Tribunal. "
            "FIXED-TERM TENANCIES: rent can only increase during a fixed term if the "
            "agreement contains an express, clear rent review clause."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # RENT REPAYMENT ORDERS
    # ════════════════════════════════════════════════════════════════
    {
        "id": "rro",
        "source": "Housing and Planning Act 2016, Chapter 3",
        "citation": "Housing and Planning Act 2016, s.40-56",
        "category": "Enforcement",
        "title": "Rent Repayment Orders — Scope, Process & Awards",
        "text": (
            "Rent Repayment Orders (RROs) are orders requiring a landlord to repay up to "
            "12 months' rent, available from the First-tier Tribunal (Property Chamber). "
            "QUALIFYING OFFENCES (landlord must have committed one of): operating an unlicensed "
            "HMO; letting a property in a selective licensing area without a licence; breaching "
            "an Improvement Notice or Emergency Remedial Action order; illegally evicting a "
            "tenant; using violence to secure entry; breaching a Banning Order. "
            "WHO CAN APPLY: the tenant (or former tenant) affected; OR the local housing "
            "authority (can apply even if no individual tenant has complained). "
            "STANDARD OF PROOF: civil standard (balance of probabilities) — the landlord does "
            "NOT need to have been convicted of the offence. "
            "AMOUNT: Tribunal must order repayment of some amount — maximum is 12 months' "
            "rent paid during the relevant period. For local authority applications — all of "
            "the rent repaid goes to the local authority. "
            "RENTERS' RIGHTS ACT 2025 EXPANSION: RRO scope extended to include: failure to "
            "register on the Landlord Portal/Property Database; breach of the Ombudsman scheme "
            "rules; serving unlawful Section 21 notices. Maximum RRO award increased."
        ),
    },

    # ════════════════════════════════════════════════════════════════
    # LEASEHOLD REFORM
    # ════════════════════════════════════════════════════════════════
    {
        "id": "lfra2024",
        "source": "Leasehold and Freehold Reform Act 2024",
        "citation": "Leasehold and Freehold Reform Act 2024 (c.22)",
        "category": "Leasehold",
        "title": "Leasehold and Freehold Reform Act 2024 — Key Provisions",
        "text": (
            "The Leasehold and Freehold Reform Act 2024 received Royal Assent on 24 May 2024. "
            "KEY PROVISIONS: "
            "LEASE EXTENSIONS: leaseholders of houses and flats now have a statutory right to "
            "extend their lease by 990 years at a peppercorn (zero) ground rent — up from 90 "
            "years for flats and 50 years for houses. The marriage value (a premium previously "
            "payable on leases under 80 years) is abolished. "
            "ELIGIBILITY: 2-year ownership requirement for statutory lease extension removed — "
            "leaseholders can extend immediately upon purchase. "
            "GROUND RENT: new leasehold houses cannot be created — prohibition on leasehold "
            "houses (except in limited circumstances including shared ownership). "
            "RIGHT TO MANAGE: process simplified — leaseholders can take over management of "
            "their building more easily; the 25% non-residential restriction increased to 50%; "
            "costs regime changed so landlords cannot automatically recover legal costs. "
            "SERVICE CHARGES: new transparency requirements — freeholders must provide detailed "
            "service charge information in a prescribed format; leaseholders can challenge "
            "unreasonable charges more easily at the First-tier Tribunal. "
            "BUILDING INSURANCE: freeholders cannot profit from insurance commissions — "
            "leaseholders have rights to challenge excessive or opaque insurance arrangements. "
            "NOTE: Leasehold is NOT abolished — leasehold flats remain. Further reforms "
            "including commonhold are expected in subsequent legislation."
        ),
    },
]
