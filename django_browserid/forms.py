"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
from django import forms


class BrowserIDForm(forms.Form):
    assertion = forms.CharField(widget=forms.HiddenInput())
    clear_browserid = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, clear_browserid=False, *args, **kwargs):
        super(BrowserIDForm, self).__init__(*args, **kwargs)
        if not clear_browserid:
            self.fields.pop('clear_browserid')

    class Media:
        js = ('browserid/browserid.js', 'https://login.persona.org/include.js')
