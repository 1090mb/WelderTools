from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from welder_tools import WeldingExpert


class WelderToolsApp(App):
    def build(self):
        self.expert = WeldingExpert()
        self.title = 'WelderTools'
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Result display
        self.result_label = Label(text='Welcome to WelderTools!', size_hint_y=None, height=400, markup=True)
        self.result_label.bind(width=lambda *x: self.result_label.setter('text_size')(self.result_label, (self.result_label.width, None)))
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.result_label)
        main_layout.add_widget(scroll_view)

        # Input layout
        input_layout = GridLayout(cols=2, size_hint_y=None, height=200, spacing=10)

        # MIG/TIG/Arc Inputs
        self.material_spinner = Spinner(text='Select Material', values=list(self.expert.materials.keys()))
        self.thickness_spinner = Spinner(text='Select Thickness')
        self.material_spinner.bind(text=self.update_thickness_spinner)

        input_layout.add_widget(self.material_spinner)
        input_layout.add_widget(self.thickness_spinner)

        # Wire Speed Inputs
        self.wire_size_spinner = Spinner(text='Select Wire Size')
        self.thickness_cat_spinner = Spinner(text='Select Thickness Category')
        self.material_spinner.bind(text=self.update_wire_spinners)

        input_layout.add_widget(self.wire_size_spinner)
        input_layout.add_widget(self.thickness_cat_spinner)

        # Machine Brand Input
        self.brand_spinner = Spinner(text='Select Brand', values=list(self.expert.machine_brands.keys()))
        input_layout.add_widget(self.brand_spinner)

        main_layout.add_widget(input_layout)

        # Button layout
        button_layout = GridLayout(cols=3, size_hint_y=None, height=150, spacing=10)

        mig_button = Button(text='MIG Settings', on_press=self.get_mig_settings)
        tig_button = Button(text='TIG Settings', on_press=self.get_tig_settings)
        arc_button = Button(text='Arc Settings', on_press=self.get_arc_settings)
        wire_button = Button(text='Wire Speed', on_press=self.get_wire_speed)
        machine_button = Button(text='Machine Info', on_press=self.get_machine_info)
        material_info_button = Button(text='Material Info', on_press=self.get_material_info)

        button_layout.add_widget(mig_button)
        button_layout.add_widget(tig_button)
        button_layout.add_widget(arc_button)
        button_layout.add_widget(wire_button)
        button_layout.add_widget(machine_button)
        button_layout.add_widget(material_info_button)

        main_layout.add_widget(button_layout)

        return main_layout

    def update_thickness_spinner(self, spinner, text):
        material = text.lower().replace(' ', '_')
        if material in self.expert.mig_settings:
            self.thickness_spinner.values = list(self.expert.mig_settings[material]['thickness_range'].keys())
        else:
            self.thickness_spinner.values = []

    def update_wire_spinners(self, spinner, text):
        material = text.lower().replace(' ', '_')
        if material in self.expert.wire_speeds:
            self.wire_size_spinner.values = list(self.expert.wire_speeds[material].keys())
            if self.wire_size_spinner.values:
                wire_size = self.wire_size_spinner.values[0]
                self.thickness_cat_spinner.values = list(self.expert.wire_speeds[material][wire_size].keys())
            else:
                self.thickness_cat_spinner.values = []
        else:
            self.wire_size_spinner.values = []
            self.thickness_cat_spinner.values = []

    def get_mig_settings(self, instance):
        self.result_label.text = self.expert.get_mig_settings(self.material_spinner.text, self.thickness_spinner.text)

    def get_tig_settings(self, instance):
        self.result_label.text = self.expert.get_tig_settings(self.material_spinner.text, self.thickness_spinner.text)

    def get_arc_settings(self, instance):
        self.result_label.text = self.expert.get_arc_settings(self.material_spinner.text, self.thickness_spinner.text)

    def get_wire_speed(self, instance):
        self.result_label.text = self.expert.get_wire_speed(self.material_spinner.text, self.wire_size_spinner.text, self.thickness_cat_spinner.text)

    def get_machine_info(self, instance):
        self.result_label.text = self.expert.get_machine_info(self.brand_spinner.text)

    def get_material_info(self, instance):
        self.result_label.text = self.expert.get_material_info(self.material_spinner.text)


if __name__ == '__main__':
    WelderToolsApp().run()
