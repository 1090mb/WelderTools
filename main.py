from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from welder_tools import WeldingExpert


class WelderToolsLayout(BoxLayout):
    pass


class WelderToolsApp(App):
    def build(self):
        self.expert = WeldingExpert()
        self.title = 'WelderTools'
        Window.clearcolor = (0.15, 0.15, 0.15, 1)
        return WelderToolsLayout()

    def get_materials(self):
        return list(self.expert.materials.keys())

    def get_brands(self):
        return list(self.expert.machine_brands.keys())

    def update_thickness_spinner(self, material):
        material = material.lower().replace(' ', '_')
        if material in self.expert.mig_settings:
            self.root.ids.thickness_spinner.values = list(self.expert.mig_settings[material]['thickness_range'].keys())
        else:
            self.root.ids.thickness_spinner.values = []

    def update_wire_spinners(self, material):
        material = material.lower().replace(' ', '_')
        if material in self.expert.wire_speeds:
            self.root.ids.wire_size_spinner.values = list(self.expert.wire_speeds[material].keys())
            if self.root.ids.wire_size_spinner.values:
                wire_size = self.root.ids.wire_size_spinner.values[0]
                if wire_size in self.expert.wire_speeds[material]:
                    self.root.ids.thickness_cat_spinner.values = list(self.expert.wire_speeds[material][wire_size].keys())
                else:
                    self.root.ids.thickness_cat_spinner.values = []
            else:
                self.root.ids.thickness_cat_spinner.values = []
        else:
            self.root.ids.wire_size_spinner.values = []
            self.root.ids.thickness_cat_spinner.values = []

    def get_mig_settings(self):
        self.root.ids.result_label.text = self.expert.get_mig_settings(self.root.ids.material_spinner.text, self.root.ids.thickness_spinner.text)

    def get_tig_settings(self):
        self.root.ids.result_label.text = self.expert.get_tig_settings(self.root.ids.material_spinner.text, self.root.ids.thickness_spinner.text)

    def get_arc_settings(self):
        self.root.ids.result_label.text = self.expert.get_arc_settings(self.root.ids.material_spinner.text, self.root.ids.thickness_spinner.text)

    def get_wire_speed(self):
        self.root.ids.result_label.text = self.expert.get_wire_speed(self.root.ids.material_spinner.text, self.root.ids.wire_size_spinner.text, self.root.ids.thickness_cat_spinner.text)

    def get_machine_info(self):
        self.root.ids.result_label.text = self.expert.get_machine_info(self.root.ids.brand_spinner.text)

    def get_material_info(self):
        self.root.ids.result_label.text = self.expert.get_material_info(self.root.ids.material_spinner.text)


if __name__ == '__main__':
    WelderToolsApp().run()
