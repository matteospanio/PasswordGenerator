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

from gi.repository import Gtk


@Gtk.Template(resource_path='/org/gnome/PasswordGenerator/window.ui')
class PasswordgeneratorWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'PasswordgeneratorWindow'

    # settings
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


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.symbols    = self.symbolsSwitch.get_active()
        self.numbers    = self.numbersSwitch.get_active()
        self.lowercase  = self.lowerSwitch.get_active()
        self.uppercase  = self.upperSwitch.get_active()

        #self.copyBtn.connect("clicked", self.onCopyBtnClick)


    @Gtk.Template.Callback()
    def onCopyBtnClick(self, widget, **_kwargs):
        print("Hello world!")
        
