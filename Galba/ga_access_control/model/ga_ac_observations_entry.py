# -*- encoding: utf-8 -*-

#This file is part of “Sistema de Gestión de Recursos Empresariales.
#Módulo de Control de Acceso”.
#Empresa Socialista de Capital Mixto Guardián del ALBA.

#created at 20/12/2016
#moduleauthor: Rubén Garcia <garciara@guardiandelalba.pdvsa.com>
#moduleauthor: Miguel Villamizar <villamizarm@guardiandelalba.com>

from openerp import models, fields, api, _
from datetime import datetime
from openerp.osv import osv

class ga_ac_observations_entry(models.Model):
    _name= 'ga.ac.observations.entry'
    _description= 'Observations Of Entrance'
    _rec_name = 'name_observations_e'
    name_observations_e = fields.Char(string='Observations entrance',
                                    size=100,
                                    required=True,
                                    help='Specifies the observations for Entrance.')

    #Validate the moment of delete a record it is not an assigned
    @api.multi
    def unlink(self):
        can_delete = self.env['hr.attendance'].search([('observations_entry_id','=',self.id)])
        if(len(can_delete)!=0):
            raise osv.except_osv(_('Alert!!!'), _('Sorry, this attribute cannot be deleted for it is assigned to an user'))
        else:
            return super(ga_ac_observations_entry, self).unlink()