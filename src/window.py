# window.py
#
# Copyright 2021 Matteo Spanio
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name(s) of the above copyright
# holders shall not be used in advertising or otherwise to promote the sale,
# use or other dealings in this Software without prior written
# authorization.

from gi.repository import Gtk, Gdk, Notify
from .generator import StringGenerator


@Gtk.Template(resource_path='/org/gnome/PasswordGenerator/window.ui')
class PasswordgeneratorWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'PasswordgeneratorWindow'

    # settings
    length:         int
    symbols:        bool
    numbers:        bool
    lowercase:      bool
    uppercase:      bool

    # buttons
    copyBtn:        Gtk.Button = Gtk.Template.Child()
    generateBtn:    Gtk.Button = Gtk.Template.Child()

    # switches
    symbolsSwitch:  Gtk.Switch = Gtk.Template.Child()
    numbersSwitch:  Gtk.Switch = Gtk.Template.Child()
    lowerSwitch:    Gtk.Switch = Gtk.Template.Child()
    upperSwitch:    Gtk.Switch = Gtk.Template.Child()

    # entries
    pwdLength:      Gtk.Entry  = Gtk.Template.Child()

    # display
    pwdView:        Gtk.Label  = Gtk.Template.Child()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.length     = 0

        self.symbols    = self.symbolsSwitch.get_active()
        self.numbers    = self.numbersSwitch.get_active()
        self.lowercase  = self.lowerSwitch.get_active()
        self.uppercase  = self.upperSwitch.get_active()

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)



    @Gtk.Template.Callback()
    def onCopyBtnClick(self, widget, **_kwargs):
        """
        copies password to clipboard
        """
        self.clipboard.set_text(self.pwdView.get_text(), -1)

        # FIXME: notification system doesnt work
        n = Notify.Notification.new("Success","Password copied to clipboard!")
        n.show()


    @Gtk.Template.Callback()
    def onGenerateBtnClick(self, widget, **_kwargs):
        """
        generates the password
        """
        generator = StringGenerator(self.length, self.uppercase,
                                    self.lowercase, self.numbers,
                                    self.symbols, False)
        self.pwdView.set_text(generator.generate())


    @Gtk.Template.Callback()
    def onEntryKeypress(self, widget, event):
        """
        when you write a number in the entry self.length is updated
        """
        self.length = 0 if self.pwdLength.get_text() == '' else int(self.pwdLength.get_text())


    @Gtk.Template.Callback()
    def onSymbolsSwitch(self, widget, gparam):
        self.symbols = self.symbolsSwitch.get_active()


    @Gtk.Template.Callback()
    def onNumbersSwitch(self, widget, gparam):
        self.numbers = self.numbersSwitch.get_active()


    @Gtk.Template.Callback()
    def onLowerSwitch(self, widget, gparam):
        self.lowercase = self.lowerSwitch.get_active()


    @Gtk.Template.Callback()
    def onUpperSwitch(self, widget, gparam):
        self.uppercase = self.upperSwitch.get_active()
        
