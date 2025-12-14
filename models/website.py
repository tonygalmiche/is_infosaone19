# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.fields import Domain

import logging
_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = "website"

    def _compute_menu(self):
        _logger.info("=== DEBUG _compute_menu ===")
        _logger.info(f"Websites: {self.ids}")
        
        # prefetch all accessible menus at once
        all_menus = self.env['website.menu'].search_fetch(Domain('website_id', 'in', self.ids))
        _logger.info(f"All menus found: {all_menus.ids}")
        _logger.info(f"All menus details: {[(m.id, m.name, m.parent_id.id if m.parent_id else None, m.website_id.id if m.website_id else None) for m in all_menus]}")

        for website in self:
            menus = all_menus.filtered(lambda m: m.website_id == website)
            _logger.info(f"Website {website.id} - Menus filtered: {menus.ids}")

            # use field parent_id (1 query) to determine field child_id (2 queries by level)"
            children = dict.fromkeys(menus, ())
            for menu in menus:
                # don't add child menu if parent is forbidden
                if menu.parent_id and menu.parent_id in menus:
                    children[menu.parent_id] += (menu.id,)
            for menu, child_items in children.items():
                menu._fields['child_id']._update_cache(menu, child_items)

            # prefetch every website.page and ir.ui.view at once
            menus.mapped('is_visible')

            top_menus = menus.filtered(lambda m: not m.parent_id)
            _logger.info(f"Website {website.id} - Top menus (no parent): {top_menus.ids}")
            _logger.info(f"Website {website.id} - Top menus names: {[m.name for m in top_menus]}")
            
            website.menu_id = top_menus[:1].id
            _logger.info(f"Website {website.id} - menu_id set to: {website.menu_id.id if website.menu_id else None}")
        
        _logger.info("=== END DEBUG _compute_menu ===")
