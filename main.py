import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from welder_tools import WeldingExpert

# Compact KV Layout with Inheritance
KV = """
<BaseBtn@Button>:
    background_color: 0.2, 0.6, 0.8, 1
    size_hint_y: 0.1

<TitleLbl@Label>:
    font_size: '24sp'
    color: 0.9, 0.6, 0.2, 1
    size_hint_y: 0.1

<ScrollLbl@Label>:
    text_size: self.width, None
    size_hint_y: None
    height: self.texture_size[1]
    halign: 'left'
    valign: 'top'
    padding: 10, 10

ScreenManager:
    MainMenuScreen:
    WeldingSettingsScreen:
    WireSpeedScreen:
    MachineInfoScreen:
    MaterialScreen:
    TrackingScreen:

<MainMenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        canvas.before:
            Color: rgba: 0.1, 0.1, 0.1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'WelderTools'
            font_size: '32sp'
            bold: True
            color: 0.9, 0.6, 0.2, 1
            size_hint_y: 0.25
        BaseBtn:
            text: 'Welding Settings'
            on_release: app.root.current = 'settings'
        BaseBtn:
            text: 'Wire Speed Calculator'
            on_release: app.root.current = 'wirespeed'
        BaseBtn:
            text: 'Machine Info'
            on_release: app.root.current = 'machines'
        BaseBtn:
            text: 'Material Info'
            on_release: app.root.current = 'materials'
        BaseBtn:
            text: 'Tracking / Log'
            on_release: app.root.current = 'tracking'
        Widget:

<WeldingSettingsScreen>:
    name: 'settings'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        TitleLbl:
            text: 'Welding Settings'
        GridLayout:
            cols: 2
            size_hint_y: 0.25
            spacing: 10
            Label:
                text: 'Process:'
            Spinner:
                id: process_spinner
                text: 'MIG'
                values: ['MIG', 'TIG', 'Arc']
                on_text: root.update_thickness_values()
            Label:
                text: 'Material:'
            Spinner:
                id: material_spinner
                text: 'Select Material'
                values: root.get_materials()
                on_text: root.update_thickness_values()
            Label:
                text: 'Thickness:'
            Spinner:
                id: thickness_spinner
                text: 'Select Thickness'
                values: []
        BaseBtn:
            text: 'Get Settings'
            background_color: 0.2, 0.8, 0.2, 1
            on_release: root.calculate_settings()
        ScrollView:
            ScrollLbl:
                id: result_label
                text: 'Select parameters and click Get Settings'
        BaseBtn:
            text: 'Back to Menu'
            background_color: 0.8, 0.2, 0.2, 1
            on_release: app.root.current = 'menu'

<WireSpeedScreen>:
    name: 'wirespeed'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        TitleLbl:
            text: 'Wire Speed Calculator'
        GridLayout:
            cols: 2
            size_hint_y: 0.25
            spacing: 10
            Label:
                text: 'Material:'
            Spinner:
                id: ws_material_spinner
                text: 'Select Material'
                values: root.get_materials()
                on_text: root.update_wire_sizes()
            Label:
                text: 'Wire Size:'
            Spinner:
                id: wire_size_spinner
                text: 'Select Size'
                values: []
                on_text: root.update_thickness_cats()
            Label:
                text: 'Thickness:'
            Spinner:
                id: thickness_cat_spinner
                text: 'Select Category'
                values: []
        BaseBtn:
            text: 'Calculate'
            background_color: 0.2, 0.8, 0.2, 1
            on_release: root.calculate_speed()
        Label:
            id: ws_result_label
            text: ''
            text_size: self.width, None
            halign: 'center'
            valign: 'middle'
        BaseBtn:
            text: 'Back to Menu'
            background_color: 0.8, 0.2, 0.2, 1
            on_release: app.root.current = 'menu'

<MachineInfoScreen>:
    name: 'machines'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        TitleLbl:
            text: 'Machine Info'
        Spinner:
            id: brand_spinner
            text: 'Select Brand'
            values: root.get_brands()
            size_hint_y: 0.1
            on_text: root.show_info()
        ScrollView:
            ScrollLbl:
                id: machine_result_label
                text: ''
        BaseBtn:
            text: 'Back to Menu'
            background_color: 0.8, 0.2, 0.2, 1
            on_release: app.root.current = 'menu'

<MaterialScreen>:
    name: 'materials'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        TitleLbl:
            text: 'Material Info'
        Spinner:
            id: mat_info_spinner
            text: 'Select Material'
            values: root.get_materials()
            size_hint_y: 0.1
            on_text: root.show_info()
        ScrollView:
            ScrollLbl:
                id: mat_result_label
                text: ''
        BaseBtn:
            text: 'Back to Menu'
            background_color: 0.8, 0.2, 0.2, 1
            on_release: app.root.current = 'menu'

<TrackingScreen>:
    name: 'tracking'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        TitleLbl:
            text: 'Welding Log'
        ScrollView:
            ScrollLbl:
                id: log_label
                text: 'No logs yet.'
        BaseBtn:
            text: 'Refresh Log'
            on_release: root.update_log()
        BaseBtn:
            text: 'Clear Log'
            background_color: 0.8, 0.4, 0.2, 1
            on_release: root.clear_log()
        BaseBtn:
            text: 'Export to CSV'
            on_release: root.export_log()
        BaseBtn:
            text: 'Back to Menu'
            background_color: 0.8, 0.2, 0.2, 1
            on_release: app.root.current = 'menu'
"""

class MainMenuScreen(Screen): pass

class WeldingSettingsScreen(Screen):
    def get_materials(self):
        app = App.get_running_app()
        return sorted([m.replace('_', ' ').title() for m in app.expert.materials.keys()]) if hasattr(app, 'expert') else []

    def update_thickness_values(self):
        app = App.get_running_app()
        mat = self.ids.material_spinner.text.lower().replace(' ', '_')
        proc = self.ids.process_spinner.text
        vals = []
        if proc == 'MIG' and mat in app.expert.mig_settings:
            vals = list(app.expert.mig_settings[mat]['thickness_range'].keys())
        elif proc == 'TIG' and mat in app.expert.tig_settings:
            vals = list(app.expert.tig_settings[mat]['thickness_range'].keys())
        elif proc == 'Arc' and mat in app.expert.arc_settings:
            vals = list(app.expert.arc_settings[mat].get('thickness_range', {}).keys()) if mat != 'cast_iron' else ['N/A']
        
        self.ids.thickness_spinner.values = vals
        self.ids.thickness_spinner.text = vals[0] if vals else 'Select Thickness'

    def calculate_settings(self):
        app = App.get_running_app()
        proc, mat, thick = self.ids.process_spinner.text, self.ids.material_spinner.text, self.ids.thickness_spinner.text
        if mat == 'Select Material':
            self.ids.result_label.text = "Please select a material."
            return
        
        methods = {'MIG': app.expert.get_mig_settings, 'TIG': app.expert.get_tig_settings, 'Arc': app.expert.get_arc_settings}
        self.ids.result_label.text = methods[proc](mat, thick)

class WireSpeedScreen(Screen):
    def get_materials(self):
        app = App.get_running_app()
        return sorted([m.replace('_', ' ').title() for m in app.expert.wire_speeds.keys()]) if hasattr(app, 'expert') else []

    def update_wire_sizes(self):
        app = App.get_running_app()
        mat = self.ids.ws_material_spinner.text.lower().replace(' ', '_')
        if mat in app.expert.wire_speeds:
            vals = list(app.expert.wire_speeds[mat].keys())
            self.ids.wire_size_spinner.values = vals
            if vals: self.ids.wire_size_spinner.text = vals[0]; self.update_thickness_cats()

    def update_thickness_cats(self):
        app = App.get_running_app()
        mat = self.ids.ws_material_spinner.text.lower().replace(' ', '_')
        wire = self.ids.wire_size_spinner.text
        if mat in app.expert.wire_speeds and wire in app.expert.wire_speeds[mat]:
            vals = list(app.expert.wire_speeds[mat][wire].keys())
            self.ids.thickness_cat_spinner.values = vals
            if vals: self.ids.thickness_cat_spinner.text = vals[0]

    def calculate_speed(self):
        app = App.get_running_app()
        mat, wire, thick = self.ids.ws_material_spinner.text, self.ids.wire_size_spinner.text, self.ids.thickness_cat_spinner.text
        self.ids.ws_result_label.text = "Please select a material." if mat == 'Select Material' else app.expert.get_wire_speed(mat, wire, thick)

class MachineInfoScreen(Screen):
    def get_brands(self):
        app = App.get_running_app()
        return sorted(list(app.expert.machine_brands.keys())) if hasattr(app, 'expert') else []

    def show_info(self):
        app = App.get_running_app()
        brand = self.ids.brand_spinner.text
        if brand != 'Select Brand': self.ids.machine_result_label.text = app.expert.get_machine_info(brand)

class MaterialScreen(Screen):
    def get_materials(self):
        app = App.get_running_app()
        return sorted([m.replace('_', ' ').title() for m in app.expert.materials.keys()]) if hasattr(app, 'expert') else []

    def show_info(self):
        app = App.get_running_app()
        mat = self.ids.mat_info_spinner.text
        if mat != 'Select Material': self.ids.mat_result_label.text = app.expert.get_material_info(mat)

class TrackingScreen(Screen):
    def on_enter(self): self.update_log()
    def update_log(self):
        app = App.get_running_app()
        if hasattr(app, 'expert'): self.ids.log_label.text = app.expert.view_log()
    def clear_log(self):
        app = App.get_running_app()
        if hasattr(app, 'expert'): app.expert.clear_log(); self.update_log()
    def export_log(self):
        app = App.get_running_app()
        if hasattr(app, 'expert'):
            path = os.path.join(app.user_data_dir, 'welding_log_export.csv')
            res = app.expert.export_log_to_csv(path)
            self.ids.log_label.text = res + "\n\n" + self.ids.log_label.text

class WelderToolsApp(App):
    def build(self):
        if not os.path.exists(self.user_data_dir): os.makedirs(self.user_data_dir)
        self.expert = WeldingExpert(log_file=os.path.join(self.user_data_dir, 'welding_log.json'))
        self.title = 'WelderTools'
        Window.clearcolor = (0.15, 0.15, 0.15, 1)
        return Builder.load_string(KV)

if __name__ == '__main__': WelderToolsApp().run()
