def get_employees() -> dict[str, int]:
    print("-- get_employees executed")

    return {
        "Morten": 54,
        "Nanna": 27,
        "Simon": 23,
        "Sarah": 26,
        "Lasse": 42
    }

def get_employee_maternity_rules() -> str:
    return """
Employee Maternity and Parental Leave Policy


Employee Maternity and Parental Leave Policy
1. Purpose
The purpose of this policy is to provide employees with clear information about maternity leave, parental leave, pregnancy-related workplace considerations, and the process for requesting and returning from leave.

The company is committed to supporting employees during pregnancy, childbirth, and the period following the birth or adoption of a child. Employees should be treated fairly and respectfully throughout this period, and employment decisions should not be based on pregnancy, maternity leave, or an employee's lawful use of parental leave rights.

This policy should be read together with applicable employment legislation, employment contracts, collective agreements, and any other applicable company policies. Where mandatory law provides greater rights or protections than this policy, the applicable law will take precedence.

2. Eligibility
Employees may be entitled to maternity and/or parental leave depending on their employment status, length of employment, applicable legislation, and other relevant circumstances.

Employees are encouraged to contact Human Resources as early as reasonably possible when they know that they will require maternity or parental leave. HR can provide information about the company's procedures and the documentation that may be required.

The company will handle information relating to pregnancy, childbirth, and parental leave confidentially and only share it with individuals who need the information for legitimate employment or administrative purposes.

3. Notification of Pregnancy
Employees are not required to disclose a pregnancy earlier than required by applicable law or workplace safety considerations. However, employees are encouraged to notify their manager or HR when they feel comfortable doing so, particularly where workplace adjustments may be necessary.

Early communication can help the company plan workloads, temporary staffing, leave arrangements, and any appropriate workplace accommodations.

An employee should not be disadvantaged because they have informed the company about a pregnancy.

4. Maternity Leave
Maternity leave is leave associated with pregnancy and childbirth. The duration, timing, compensation, and eligibility requirements for maternity leave are determined by applicable legislation and, where applicable, the employee's contract or collective agreement.

Employees should provide the company with the expected start date of maternity leave as soon as reasonably possible once that date is known.

The company will make reasonable efforts to plan for the employee's absence while respecting the employee's rights and privacy.

Where medical circumstances require an employee to stop working earlier than originally planned, the company will cooperate with the employee and follow applicable legal requirements.

5. Parental Leave
Following maternity leave, an employee may have rights to parental leave or other forms of family-related leave.

Parental leave may also be available to parents who are not the birth parent, depending on applicable law.

Employees should submit requests for parental leave according to the company's normal procedures and applicable statutory notice requirements.

Where an employee changes their planned return date or leave period, they should notify HR as soon as reasonably possible.

6. Pregnancy-Related Workplace Adjustments
The company will consider appropriate workplace adjustments where pregnancy or pregnancy-related circumstances affect an employee's ability to safely perform particular duties.

Depending on the employee's role and applicable requirements, adjustments may include changes to working hours, temporary changes in duties, additional breaks, changes to physical activities, or other reasonable measures.

Any adjustment should be discussed with the employee and implemented in accordance with applicable law and occupational health and safety requirements.

Employees should inform their manager or HR if they believe that a workplace activity could present a health or safety concern during pregnancy.

7. Medical Appointments
Employees may need medical appointments before and after childbirth. The company will handle pregnancy-related medical appointments in accordance with applicable legislation and company procedures.

Employees should provide reasonable notice of appointments whenever possible so that work can be planned appropriately.

Where documentation is legally required, employees should provide the appropriate documentation through the company's normal process.
"""
employee_tools = [
       {
                "type" : "function",
                "name" : "get_employees",
                "description" : """
                    List all employees
                    -------------------
                    Outputs: python: dict[str,int] (employee names, age)
                """,
                "parameters" : {
                    "type" : "object",
                    "properties" : {},
                    "required" : [ ],
                    "additionalProperties" : False
                }
            },
             {
                            "type" : "function",
                            "name" : "get_employee_maternity_rules",
                            "description" : """
                                Get a verbose document about the company's maternity rules
                                -------------------
                                Outputs: string
                            """,
                            "parameters" : {
                                "type" : "object",
                                "properties" : {},
                                "required" : [ ],
                                "additionalProperties" : False
                            }
            }
]