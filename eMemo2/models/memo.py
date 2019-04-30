from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import datetime

import logging
_logger = logging.getLogger(__name__)


class memo (models.Model):
    _name = 'x_memo'
    _inherit = 'mail.thread'
    x_currency_id = fields.Many2one(string="Currency", comodel_name="res.currency", required=False, index=True,track_visibility=True)
    x_name = fields.Char(string="Name",  required=False, index=True, track_visibility=True)
    x_studio_background = fields.Text(string="Background",  required=False, index=True,   track_visibility=True)
    x_studio_budget = fields.Monetary(string="Budget",  required=False, index=True,  track_visibility=True)
    x_studio_campaign_responses = fields.Text(string="Campaign Responses",  required=False, index=True,track_visibility=True)
    x_studio_campaign_scenarios = fields.Text(string="Campaign Scenarios",  required=False, index=True,track_visibility=True)
    x_studio_cco_approval = fields.Many2one(string="CCO Approval", comodel_name="res.users", required=False, index=True,track_visibility=True)
    x_studio_cco_approval_date = fields.Datetime(string="CCO Approval Date",  required=False,  index=True, track_visibility=True)
    x_studio_cdo_approval = fields.Many2one(string="CDO Approval", comodel_name="res.users", required=False, index=True,track_visibility=True)
    x_studio_cdo_approval_date = fields.Datetime(string="CDO Approval Date",  required=False,  index=True, track_visibility=True)
    x_studio_ceo_approval = fields.Many2one(string="CEO Approval", comodel_name="res.users", required=False, index=True,track_visibility=True)
    x_studio_ceo_approval_date = fields.Datetime(string="CEO Approval Date",  required=False,  index=True, track_visibility=True)
    x_studio_compliance_approval = fields.Many2one(string="Compliance Approval", comodel_name="res.users",    required=False, index=True, track_visibility=True)
    x_studio_compliance_approval_date = fields.Datetime(string="Compliance Approval Date",  required=False, index=True, track_visibility=True)
    x_studio_finance_approval = fields.Many2one(string="Finance Approval", comodel_name="res.users", required=False, index=True, track_visibility=True)
    x_studio_finance_approval_date = fields.Datetime(string="Finance Approval Date",  required=False,      index=True, track_visibility=True)
    x_studio_financial_assumption = fields.Html(string="Financial Assumption",  required=False, index=True, track_visibility=True)
    x_studio_hod_approval = fields.Many2one(string="HOD Approval", comodel_name="res.users", required=False, index=True,track_visibility=True)
    x_studio_hod_approval_date = fields.Datetime(string="HOD Approval Date",  required=False,  index=True, track_visibility=True)
    x_studio_hod_review = fields.Many2one(string="HOD Review", comodel_name="res.users", required=False, index=True,      track_visibility=True)
    x_studio_hod_review_date = fields.Datetime(string="HOD Review Date",  required=False, index=True,track_visibility=True)
    x_studio_legal_approval = fields.Many2one(string="Legal Approval", comodel_name="res.users", required=False,  index=True, track_visibility=True)
    x_studio_legal_approval_date = fields.Datetime(string="Legal Approval Date",  required=False,    index=True, track_visibility=True)
    x_studio_manager_approval = fields.Many2one(string="Manager Approval", comodel_name="res.users", required=False, index=True, track_visibility=True)
    x_studio_manager_approval_date = fields.Datetime(string="Manager Approval Date",  required=False,      index=True, track_visibility=True)
    x_studio_mancom_approval = fields.Many2one(string="Mancom Approval", comodel_name="res.users", required=False,index=True, track_visibility=True)
    x_studio_mancom_approval_date = fields.Datetime(string="Mancom Approval Date",  required=False,     index=True, track_visibility=True)
    x_studio_marketing_hod_approval = fields.Many2one(string="Marketing HOD Approval", comodel_name="res.users",       required=False, index=True, track_visibility=True)
    x_studio_marketing_hod_approval_date = fields.Datetime(string="Marketing HOD Approval Date",  required=False, index=True, track_visibility=True)
    x_studio_marketing_manager_approval = fields.Many2one(string="Marketing Manager Approval", comodel_name="res.users",required=False, index=True, track_visibility=True)
    x_studio_marketing_manager_approval_date = fields.Datetime(string="Marketing Manager Approval Date",      required=False, index=True,     track_visibility=True)
    x_studio_marketing_team = fields.Many2one(string="Marketing Team ", comodel_name="res.users", required=False,  index=True, track_visibility=True)
    x_studio_marketing_team_date = fields.Datetime(string="Marketing Team  Date",  required=False,    index=True, track_visibility=True)
    x_studio_objective = fields.Text(string="Objective",  required=False, index=True,  track_visibility=True)
    x_studio_owner_1st_review = fields.Many2one(string="Owner 1st Review", comodel_name="res.users", required=False, index=True, track_visibility=True)
    x_studio_owner_1st_review_date = fields.Datetime(string="Owner 1st Review Date",  required=False,      index=True, track_visibility=True)
    x_studio_owner_2nd_review = fields.Many2one(string="Owner 2nd Review", comodel_name="res.users", required=False, index=True, track_visibility=True)
    x_studio_owner_2nd_review_date = fields.Datetime(string="Owner 2nd Review Date",  required=False,      index=True, track_visibility=True)
    x_studio_risk_approval = fields.Many2one(string="Risk Approval", comodel_name="res.users", required=False, index=True, track_visibility=True)
    x_studio_risk_approval_date = fields.Datetime(string="Risk Approval Date",  required=False,   index=True, track_visibility=True)
    x_studio_status = fields.Selection(string="Status",  required=False, index=True, selection=[["S1","New"],["S2","Manager Approval"],["S3","Marketing Manager Approval"],["S4","Marketing HOD Approval"],["S5","HOD Review"],["S6","CDO Approval"],["S7","Finance Approval"],["S8","HOD Approval"],["S9","CEO Approval"],["S10","Mancom Approval"],["S11","CCO Approval"],["S12","Marketing Activity "],["S13","Owner 1st Review"],["S14","Legal\Compliance\Risk"],["S15","Owner 2nd Review"],["S16","Approved"],["S17","Rejected"],["S18","Need More Info"] ]  ,track_visibility=True ,default = 'S1')
    x_studio_submit_date = fields.Datetime(string="Submit Date",  required=False, index=True,       track_visibility=True)
    x_studio_submitted_by = fields.Many2one(string="Submitted By ", comodel_name="res.users", required=False,index=True, track_visibility=True)
    x_studio_test = fields.Boolean(string="test",  required=False, index=True, track_visibility=True)
    x_studio_channels = fields.Many2many(comodel_name="x_channels", string="Channels")
    x_studio_reject_by = fields.Many2one(string="Rejected By", comodel_name="res.users", required=False,
                                                index=True, track_visibility=True)
    x_studio_reject_date = fields.Datetime(string="Rejection Date", required=False, index=True,
                                                     track_visibility=True)

    x_studio_purpose = fields.Text(string="Campaign Purpose", required=False, index=True,track_visibility=True)
    x_studio_markting_branding = fields.Text(string="Marketing And Branding", required=False, index=True, track_visibility=True)
    x_file_script = fields.Binary(string="Upload Script")
    x_file_visual = fields.Binary(string="Upload Visual")
    x_file_video = fields.Binary(string="Upload Video")
    x_file_att = fields.Binary(string="Upload Attachment")
    x_roi  = fields.Float(string="ROI %", required=False)
    x_cost_to_income = fields.Float(string="Cost to Income", required=False)
    x_who_need_info = fields.Many2one(string="More Info Requested by ", comodel_name="res.users", required=False,index=True, track_visibility=True)
    x_need_info_date = fields.Datetime(string="More Info Requested date", required=False, index=True,track_visibility=True)
    x_status_after_info  = fields.Char(string="status_after_info", required=False, index=False, track_visibility=False)
    x_startdate = fields.Datetime(string="Campaign Start Date", required=True, index=True,track_visibility=True)
    x_enddate = fields.Datetime(string="Campaign End Date", required=True, index=True, track_visibility=True)

    @api.multi
    def reject(self):
        self.iselig()
        self.x_studio_status = "S17"
        self.x_studio_reject_date = datetime.datetime.now()
        self.x_studio_reject_by = self.env.uid

    def moreinfo(self):
        self.iselig()
        self.x_status_after_info = self.x_studio_status
        self.x_studio_status = "S18"
        self.x_need_info_date = datetime.datetime.now()
        self.x_who_need_info = self.env.uid

    def iselig(self):
        Agent = self.env['res.groups'].search([('name', '=', 'Agent')])
        CCO = self.env['res.groups'].search([('name', '=', 'CCO')])
        CDO = self.env['res.groups'].search([('name', '=', 'CDO')])
        CEO = self.env['res.groups'].search([('name', '=', 'CEO')])

        FinanceAgent = self.env['res.groups'].search([('name', '=', 'Finance Agent')])
        HOD = self.env['res.groups'].search([('name', '=', 'HOD')])

        Manager = self.env['res.groups'].search([('name', '=', 'Manager')])
        Mancom = self.env['res.groups'].search([('name', '=', 'Mancom')])
        MarketingAgent = self.env['res.groups'].search([('name', '=', 'Marketing Agent')])
        MarketingHOD = self.env['res.groups'].search([('name', '=', 'Marketing HOD')])
        MarketingManager = self.env['res.groups'].search([('name', '=', 'Marketing Manager')])
        Risk = self.env['res.groups'].search([('name', '=', 'Risk')])
        Legal = self.env['res.groups'].search([('name', '=', 'Legal')])
        Compliance = self.env['res.groups'].search([('name', '=', 'Compliance')])
        if self.x_studio_status == "S2":  # Manager
            if (self.env.user.id not in Manager.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

        elif self.x_studio_status == "S3":  # MarketingManager
            if (self.env.user.id not in MarketingManager.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

        elif self.x_studio_status == "S4":  # MarketingHOD
            if (self.env.user.id not in MarketingHOD.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

        elif self.x_studio_status == "S5":  # HOD Review
            if (self.env.user.id not in HOD.users.ids):
                raise ValidationError("Not Eligiable to take this Action")


        elif self.x_studio_status == "S6":
            if (self.env.user.id not in CDO.users.ids):
                raise ValidationError("Not Eligiable to take this Action")
        elif self.x_studio_status == "S7":  # FinanceAgent
            if (self.env.user.id not in FinanceAgent.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

        elif self.x_studio_status == "S8":  # HOD Approval
            if (self.env.user.id not in HOD.users.ids):
                raise ValidationError("Not Eligiable to take this Action")
        elif self.x_studio_status == "S9":  # CEO
            if (self.env.user.id not in CEO.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

        elif self.x_studio_status == "S10":  # Mancom
            if (self.env.user.id not in Mancom.users.ids):
                raise ValidationError("Not Eligiable to take this Action")


        elif self.x_studio_status == "S11":  # CCO
            if (self.env.user.id not in CCO.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

        elif self.x_studio_status == "S12":  # MarketingAgent
            if (self.env.user.id not in MarketingAgent.users.ids):
                raise ValidationError("Not Eligiable to take this Action")
        elif self.x_studio_status == "S13":  # owner 1st
            if (self.x_studio_submitted_by.id != self.env.user.id):
                raise ValidationError("Not Eligiable to take this Action")

        elif self.x_studio_status == "S14":  # Marketing
            if (self.env.user.id in Risk.users.ids or self.env.user.id in Legal.users.ids or self.env.user.id in Compliance.users.ids):
                pass
            else:
                raise ValidationError("Not Eligiable to take this Action")



        elif self.x_studio_status == "S15":  # Owner 2nd
            if (self.x_studio_submitted_by.id != self.env.user.id):
                raise ValidationError("Not Eligiable to take this Action")
        elif self.x_studio_status == "S18":
            if (self.x_studio_submitted_by.id != self.env.user.id):
                raise ValidationError("Not Eligiable to take this Action")

    '''
    New	S1
    Manager Approval	S2
    Marketing Manager Approval	S3
    Marketing HOD Approval	S4
    HOD Review	S5
    CDO Approval	S6
    Finance Approval	S7
    HOD Approval	S8
    CEO Approval	S9
    Mancom Approval	S10
    CCO Approval	S11
    Marketing Team 	S12
    Owner 1st Review	S13
    Legal\Compliance\Risk	S14
    Owner 2nd Review	S15

    '''

    @api.multi
    def approv(self):
        Agent = self.env['res.groups'].search([('name', '=', 'Agent')])
        CCO = self.env['res.groups'].search([('name', '=', 'CCO')])
        CDO = self.env['res.groups'].search([('name', '=', 'CDO')])
        CEO = self.env['res.groups'].search([('name', '=', 'CEO')])

        FinanceAgent = self.env['res.groups'].search([('name', '=', 'Finance Agent')])
        HOD = self.env['res.groups'].search([('name', '=', 'HOD')])

        Manager = self.env['res.groups'].search([('name', '=', 'Manager')])
        Mancom = self.env['res.groups'].search([('name', '=', 'Mancom')])
        MarketingAgent = self.env['res.groups'].search([('name', '=', 'Marketing Agent')])
        MarketingHOD = self.env['res.groups'].search([('name', '=', 'Marketing HOD')])
        MarketingManager = self.env['res.groups'].search([('name', '=', 'Marketing Manager')])
        Risk = self.env['res.groups'].search([('name', '=', 'Risk')])
        Legal = self.env['res.groups'].search([('name', '=', 'Legal')])
        Compliance = self.env['res.groups'].search([('name', '=', 'Compliance')])


        if not self.x_studio_status or self.x_studio_status == "S1":
            self.x_studio_status = "S2"
            self.x_studio_submit_date = datetime.datetime.now()
            self.x_studio_submitted_by = self.env.uid
        elif self.x_studio_status=="S2": #Manager
            if (self.env.user.id not in Manager.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

            self.x_studio_status="S3"
            self.x_studio_manager_approval_date =datetime.datetime.now()
            self.x_studio_manager_approval=self.env.uid
        elif self.x_studio_status == "S3":#MarketingManager
            if (self.env.user.id not in MarketingManager.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

            self.x_studio_status = "S4"
            self.x_studio_marketing_manager_approval_date = datetime.datetime.now()
            self.x_studio_marketing_manager_approval = self.env.uid
        elif self.x_studio_status == "S4":#MarketingHOD
            if (self.env.user.id not in MarketingHOD.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

            self.x_studio_status = "S5"
            self.x_studio_marketing_hod_approval_date = datetime.datetime.now()
            self.x_studio_marketing_hod_approval = self.env.uid
        elif self.x_studio_status == "S5": #HOD Review
            if (self.env.user.id not in HOD.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

            self.x_studio_status = "S6"
            self.x_studio_hod_review_date = datetime.datetime.now()
            self.x_studio_hod_review = self.env.uid

        elif self.x_studio_status == "S6":
            if (self.env.user.id not in CDO.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

            if(self.x_studio_budget==0):
                self.x_studio_status = "S8"
            else:
                self.x_studio_status = "S7"

            self.x_studio_cdo_approval_date = datetime.datetime.now()
            self.x_studio_cdo_approval = self.env.uid
        elif self.x_studio_status == "S7": #FinanceAgent
            if (self.env.user.id not in FinanceAgent.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

            self.x_studio_status = "S8"
            self.x_studio_finance_approval_date = datetime.datetime.now()
            self.x_studio_finance_approval = self.env.uid

        elif self.x_studio_status == "S8": #HOD Approval
            if (self.env.user.id not in HOD.users.ids):
                raise ValidationError("Not Eligiable to take this Action")
            if (self.x_studio_budget < 5000):
                self.x_studio_status = "S11"
            elif (self.x_studio_budget < 10000):
                self.x_studio_status = "S9"
            else:
                self.x_studio_status = "S10"

            self.x_studio_hod_approval_date = datetime.datetime.now()
            self.x_studio_hod_approval = self.env.uid

        elif self.x_studio_status == "S9": #CEO
            if (self.env.user.id not in CEO.users.ids):
                raise ValidationError("Not Eligiable to take this Action")

            self.x_studio_status = "S11"
            self.x_studio_ceo_approval_date = datetime.datetime.now()
            self.x_studio_ceo_approval = self.env.uid

        elif self.x_studio_status == "S10": #Mancom
            if (self.env.user.id not in Mancom.users.ids):
                raise ValidationError("Not Eligiable to take this Action")
            self.x_studio_status = "S11"
            self.x_studio_mancom_approval_date = datetime.datetime.now()
            self.x_studio_mancom_approval = self.env.uid


        elif self.x_studio_status == "S11": #CCO
            if (self.env.user.id not in CCO.users.ids):
                raise ValidationError("Not Eligiable to take this Action")
            self.x_studio_status = "S12"
            self.x_studio_cco_approval_date = datetime.datetime.now()
            self.x_studio_cco_approval = self.env.uid


        elif self.x_studio_status == "S12": #MarketingAgent
            if (self.env.user.id not in MarketingAgent.users.ids):
                raise ValidationError("Not Eligiable to take this Action")
            self.x_studio_status = "S13"
            self.x_studio_marketing_team_date = datetime.datetime.now()
            self.x_studio_marketing_team = self.env.uid

        elif self.x_studio_status == "S13": #owner 1st
            if (self.x_studio_submitted_by.id != self.env.user.id):
                raise ValidationError("Not Eligiable to take this Action")
            self.x_studio_status = "S14"
            self.x_studio_owner_1st_review_date = datetime.datetime.now()
            self.x_studio_owner_1st_review = self.env.uid

        elif self.x_studio_status == "S14": #Marketing
            if (self.env.user.id  in Risk.users.ids):
                self.x_studio_risk_approval_date = datetime.datetime.now()
                self.x_studio_risk_approval = self.env.uid
            elif(self.env.user.id  in Legal.users.ids):
                self.x_studio_legal_approval_date = datetime.datetime.now()
                self.x_studio_legal_approval = self.env.uid
            elif (self.env.user.id in Compliance.users.ids):
                self.x_studio_compliance_approval_date = datetime.datetime.now()
                self.x_studio_compliance_approval = self.env.uid
            else:
                raise ValidationError("Not Eligiable to take this Action")
            if(self.x_studio_compliance_approval and  self.x_studio_legal_approval and self.x_studio_risk_approval):
                self.x_studio_status = "S15"
            #self.x_studio_marketing_team_date = datetime.datetime.now()
            #self.x_studio_marketing_team = self.env.uid


        elif self.x_studio_status == "S15": #Owner 2nd
            if (self.x_studio_submitted_by.id != self.env.user.id):
                raise ValidationError("Not Eligiable to take this Action")
            self.x_studio_status = "S16"
            self.x_studio_owner_2nd_review_date = datetime.datetime.now()
            self.x_studio_owner_2nd_review = self.env.uid
        elif self.x_studio_status == "S18": #moreinfo
            if (self.x_studio_submitted_by.id != self.env.user.id):
                raise ValidationError("Not Eligiable to take this Action")
            self.x_studio_status = self.x_status_after_info



'''
New	S1
Manager Approval	S2
Marketing Manager Approval	S3
Marketing HOD Approval	S4
HOD Review	S5
CDO Approval	S6
Finance Approval	S7
HOD Approval	S8
CEO Approval	S9
Mancom Approval	S10
CCO Approval	S11
Marketing Team 	S12
Owner 1st Review	S13
Legal\Compliance\Risk	S14
Owner 2nd Review	S15

'''





