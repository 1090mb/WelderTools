#!/usr/bin/env python3
"""
WelderTools Android App
Main entry point for the Kivy-based Android application
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.spinner import Spinner

# Import the welding expert system
from welder_tools import WeldingExpert


class MainMenuScreen(Screen):
    """Main menu screen with options for different welding types and features"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        # Title
        title = Label(
            text='[b]WELDERTOOLS[/b]\nProfessional Welding Assistant',
            markup=True,
            size_hint=(1, 0.15),
            font_size='24sp',
            halign='center'
        )
        title.bind(size=title.setter('text_size'))
        layout.add_widget(title)
        
        # Main menu buttons
        buttons = [
            ('MIG Welding Settings', 'mig'),
            ('TIG Welding Settings', 'tig'),
            ('Arc/Stick Welding Settings', 'arc'),
            ('Wire Speed Calculator', 'wire'),
            ('Machine Information', 'machine'),
            ('Material Properties', 'material'),
            ('Hours & Parts Tracking', 'tracking'),
        ]
        
        for text, screen_name in buttons:
            btn = Button(
                text=text,
                size_hint=(1, 0.12),
                font_size='18sp',
                background_color=(0.2, 0.6, 0.8, 1),
                background_normal=''
            )
            btn.bind(on_press=lambda x, s=screen_name: self.go_to_screen(s))
            layout.add_widget(btn)
        
        self.add_widget(layout)
    
    def go_to_screen(self, screen_name):
        self.manager.current = screen_name


class WeldingSettingsScreen(Screen):
    """Generic screen for welding settings (MIG/TIG/Arc)"""
    
    def __init__(self, welding_type, **kwargs):
        super().__init__(**kwargs)
        self.welding_type = welding_type
        self.expert = WeldingExpert()
        
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        # Title
        title_text = f'{welding_type.upper()} Welding Settings'
        title = Label(
            text=f'[b]{title_text}[/b]',
            markup=True,
            size_hint=(1, 0.1),
            font_size='22sp'
        )
        layout.add_widget(title)
        
        # Input fields
        form_layout = GridLayout(cols=2, spacing=dp(10), size_hint=(1, 0.3))
        
        # Material selection
        form_layout.add_widget(Label(text='Material:', size_hint_x=0.4))
        self.material_spinner = Spinner(
            text='mild_steel',
            values=('mild_steel', 'stainless_steel', 'aluminum'),
            size_hint_x=0.6
        )
        form_layout.add_widget(self.material_spinner)
        
        # Thickness selection
        form_layout.add_widget(Label(text='Thickness:', size_hint_x=0.4))
        self.thickness_spinner = Spinner(
            text='1/8',
            values=('1/16', '1/8', '3/16', '1/4'),
            size_hint_x=0.6
        )
        form_layout.add_widget(self.thickness_spinner)
        
        layout.add_widget(form_layout)
        
        # Get Settings button
        btn = Button(
            text='Get Settings',
            size_hint=(1, 0.1),
            font_size='18sp',
            background_color=(0.2, 0.8, 0.2, 1),
            background_normal=''
        )
        btn.bind(on_press=self.get_settings)
        layout.add_widget(btn)
        
        # Results area
        scroll = ScrollView(size_hint=(1, 0.4))
        self.result_label = Label(
            text='Select material and thickness, then tap "Get Settings"',
            size_hint_y=None,
            markup=True,
            halign='left',
            valign='top',
            padding=(dp(10), dp(10))
        )
        self.result_label.bind(
            texture_size=self.result_label.setter('size'),
            size=self.result_label.setter('text_size')
        )
        scroll.add_widget(self.result_label)
        layout.add_widget(scroll)
        
        # Back button
        back_btn = Button(
            text='← Back to Menu',
            size_hint=(1, 0.1),
            font_size='16sp',
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal=''
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
    
    def get_settings(self, instance):
        """Fetch and display welding settings"""
        material = self.material_spinner.text
        thickness = self.thickness_spinner.text
        
        # Get settings from expert system
        if self.welding_type == 'mig':
            result = self.expert.get_mig_settings(material, thickness)
        elif self.welding_type == 'tig':
            result = self.expert.get_tig_settings(material, thickness)
        elif self.welding_type == 'arc':
            result = self.expert.get_arc_settings(material, thickness)
        else:
            result = "Unknown welding type"
        
        # Format for display
        formatted_result = result.replace('=', '').replace('\n\n', '\n')
        self.result_label.text = formatted_result


class WireSpeedScreen(Screen):
    """Wire speed calculator screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expert = WeldingExpert()
        
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        # Title
        title = Label(
            text='[b]Wire Speed Calculator[/b]',
            markup=True,
            size_hint=(1, 0.1),
            font_size='22sp'
        )
        layout.add_widget(title)
        
        # Input fields
        form_layout = GridLayout(cols=2, spacing=dp(10), size_hint=(1, 0.3))
        
        form_layout.add_widget(Label(text='Material:', size_hint_x=0.4))
        self.material_spinner = Spinner(
            text='mild_steel',
            values=('mild_steel', 'stainless_steel', 'aluminum'),
            size_hint_x=0.6
        )
        form_layout.add_widget(self.material_spinner)
        
        form_layout.add_widget(Label(text='Wire Size:', size_hint_x=0.4))
        self.wire_spinner = Spinner(
            text='0.030',
            values=('0.023', '0.030', '0.035', '0.045'),
            size_hint_x=0.6
        )
        form_layout.add_widget(self.wire_spinner)
        
        form_layout.add_widget(Label(text='Category:', size_hint_x=0.4))
        self.category_spinner = Spinner(
            text='medium',
            values=('thin', 'medium', 'thick'),
            size_hint_x=0.6
        )
        form_layout.add_widget(self.category_spinner)
        
        layout.add_widget(form_layout)
        
        # Calculate button
        btn = Button(
            text='Calculate',
            size_hint=(1, 0.1),
            font_size='18sp',
            background_color=(0.2, 0.8, 0.2, 1),
            background_normal=''
        )
        btn.bind(on_press=self.calculate)
        layout.add_widget(btn)
        
        # Results area
        scroll = ScrollView(size_hint=(1, 0.4))
        self.result_label = Label(
            text='Select parameters and tap "Calculate"',
            size_hint_y=None,
            markup=True,
            halign='left',
            valign='top',
            padding=(dp(10), dp(10))
        )
        self.result_label.bind(
            texture_size=self.result_label.setter('size'),
            size=self.result_label.setter('text_size')
        )
        scroll.add_widget(self.result_label)
        layout.add_widget(scroll)
        
        # Back button
        back_btn = Button(
            text='← Back to Menu',
            size_hint=(1, 0.1),
            font_size='16sp',
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal=''
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
    
    def calculate(self, instance):
        """Calculate wire speed"""
        material = self.material_spinner.text
        wire_size = self.wire_spinner.text
        category = self.category_spinner.text
        
        result = self.expert.get_wire_speed(material, wire_size, category)
        formatted_result = result.replace('=', '').replace('\n\n', '\n')
        self.result_label.text = formatted_result


class MachineInfoScreen(Screen):
    """Machine information screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expert = WeldingExpert()
        
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        # Title
        title = Label(
            text='[b]Machine Information[/b]',
            markup=True,
            size_hint=(1, 0.1),
            font_size='22sp'
        )
        layout.add_widget(title)
        
        # Brand selection
        brand_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=dp(10))
        brand_layout.add_widget(Label(text='Select Brand:', size_hint_x=0.4))
        self.brand_spinner = Spinner(
            text='Miller',
            values=('Miller', 'Lincoln', 'ESAB', 'Hobart', 'Everlast', 'Fronius', 'All'),
            size_hint_x=0.6
        )
        self.brand_spinner.bind(text=self.update_info)
        brand_layout.add_widget(self.brand_spinner)
        layout.add_widget(brand_layout)
        
        # Results area
        scroll = ScrollView(size_hint=(1, 0.7))
        self.result_label = Label(
            text='',
            size_hint_y=None,
            markup=True,
            halign='left',
            valign='top',
            padding=(dp(10), dp(10))
        )
        self.result_label.bind(
            texture_size=self.result_label.setter('size'),
            size=self.result_label.setter('text_size')
        )
        scroll.add_widget(self.result_label)
        layout.add_widget(scroll)
        
        # Back button
        back_btn = Button(
            text='← Back to Menu',
            size_hint=(1, 0.1),
            font_size='16sp',
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal=''
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
        
        # Load initial info
        self.update_info(self.brand_spinner, 'Miller')
    
    def update_info(self, spinner, text):
        """Update machine info display"""
        if text == 'All':
            result = self.expert.get_machine_info()
        else:
            result = self.expert.get_machine_info(text)
        formatted_result = result.replace('=', '').replace('\n\n', '\n')
        self.result_label.text = formatted_result


class MaterialScreen(Screen):
    """Material properties screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expert = WeldingExpert()
        
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        # Title
        title = Label(
            text='[b]Material Properties[/b]',
            markup=True,
            size_hint=(1, 0.1),
            font_size='22sp'
        )
        layout.add_widget(title)
        
        # Material selection
        material_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=dp(10))
        material_layout.add_widget(Label(text='Select Material:', size_hint_x=0.4))
        self.material_spinner = Spinner(
            text='mild_steel',
            values=('mild_steel', 'stainless_steel', 'aluminum', 'cast_iron'),
            size_hint_x=0.6
        )
        self.material_spinner.bind(text=self.update_info)
        material_layout.add_widget(self.material_spinner)
        layout.add_widget(material_layout)
        
        # Results area
        scroll = ScrollView(size_hint=(1, 0.7))
        self.result_label = Label(
            text='',
            size_hint_y=None,
            markup=True,
            halign='left',
            valign='top',
            padding=(dp(10), dp(10))
        )
        self.result_label.bind(
            texture_size=self.result_label.setter('size'),
            size=self.result_label.setter('text_size')
        )
        scroll.add_widget(self.result_label)
        layout.add_widget(scroll)
        
        # Back button
        back_btn = Button(
            text='← Back to Menu',
            size_hint=(1, 0.1),
            font_size='16sp',
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal=''
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
        
        # Load initial info
        self.update_info(self.material_spinner, 'mild_steel')
    
    def update_info(self, spinner, text):
        """Update material info display"""
        result = self.expert.get_material_info(text)
        formatted_result = result.replace('=', '').replace('\n\n', '\n')
        self.result_label.text = formatted_result


class TrackingScreen(Screen):
    """Hours and parts tracking screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expert = WeldingExpert()
        
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        # Title
        title = Label(
            text='[b]Hours & Parts Tracking[/b]',
            markup=True,
            size_hint=(1, 0.08),
            font_size='22sp'
        )
        layout.add_widget(title)
        
        # Log entry form
        log_layout = GridLayout(cols=2, spacing=dp(10), size_hint=(1, 0.2))
        
        log_layout.add_widget(Label(text='Hours:', size_hint_x=0.3))
        self.hours_input = TextInput(
            text='',
            multiline=False,
            input_filter='float',
            size_hint_x=0.7,
            hint_text='e.g. 4.5'
        )
        log_layout.add_widget(self.hours_input)
        
        log_layout.add_widget(Label(text='Parts:', size_hint_x=0.3))
        self.parts_input = TextInput(
            text='',
            multiline=False,
            input_filter='int',
            size_hint_x=0.7,
            hint_text='e.g. 12'
        )
        log_layout.add_widget(self.parts_input)
        
        log_layout.add_widget(Label(text='Description:', size_hint_x=0.3))
        self.desc_input = TextInput(
            text='',
            multiline=False,
            size_hint_x=0.7,
            hint_text='Optional description'
        )
        log_layout.add_widget(self.desc_input)
        
        layout.add_widget(log_layout)
        
        # Action buttons
        button_layout = GridLayout(cols=3, spacing=dp(10), size_hint=(1, 0.1))
        
        log_btn = Button(
            text='Log Entry',
            background_color=(0.2, 0.8, 0.2, 1),
            background_normal=''
        )
        log_btn.bind(on_press=self.log_entry)
        button_layout.add_widget(log_btn)
        
        stats_btn = Button(
            text='View Stats',
            background_color=(0.2, 0.6, 0.8, 1),
            background_normal=''
        )
        stats_btn.bind(on_press=self.view_stats)
        button_layout.add_widget(stats_btn)
        
        clear_btn = Button(
            text='Clear Log',
            background_color=(0.8, 0.2, 0.2, 1),
            background_normal=''
        )
        clear_btn.bind(on_press=self.clear_log)
        button_layout.add_widget(clear_btn)
        
        layout.add_widget(button_layout)
        
        # Results area
        scroll = ScrollView(size_hint=(1, 0.52))
        self.result_label = Label(
            text='Enter hours and parts to log an entry',
            size_hint_y=None,
            markup=True,
            halign='left',
            valign='top',
            padding=(dp(10), dp(10))
        )
        self.result_label.bind(
            texture_size=self.result_label.setter('size'),
            size=self.result_label.setter('text_size')
        )
        scroll.add_widget(self.result_label)
        layout.add_widget(scroll)
        
        # Back button
        back_btn = Button(
            text='← Back to Menu',
            size_hint=(1, 0.1),
            font_size='16sp',
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal=''
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
        
        # Load existing log
        self.view_stats(None)
    
    def log_entry(self, instance):
        """Log a new tracking entry"""
        try:
            # Validate hours first
            if not self.hours_input.text:
                self.result_label.text = 'Error: Please enter hours worked'
                return
            
            try:
                hours = float(self.hours_input.text)
            except ValueError:
                self.result_label.text = 'Error: Hours must be a valid number (e.g., 4.5)'
                return
            
            # Validate parts
            if not self.parts_input.text:
                self.result_label.text = 'Error: Please enter parts made'
                return
            
            try:
                parts = int(self.parts_input.text)
            except ValueError:
                self.result_label.text = 'Error: Parts must be a valid number (e.g., 12)'
                return
            
            description = self.desc_input.text or ''
            
            result = self.expert.log_hours(hours, parts, description)
            self.result_label.text = result.replace('=', '').replace('\n\n', '\n')
            
            # Clear inputs
            self.hours_input.text = ''
            self.parts_input.text = ''
            self.desc_input.text = ''
            
            # Refresh stats
            self.view_stats(None)
        except Exception as e:
            self.result_label.text = f'Error: {str(e)}'
    
    def view_stats(self, instance):
        """View tracking statistics"""
        stats = self.expert.view_stats()
        entries = self.expert.view_log(limit=10)
        
        combined = stats + '\n\n' + entries
        formatted = combined.replace('=', '').replace('\n\n', '\n')
        self.result_label.text = formatted
    
    def clear_log(self, instance):
        """Clear the tracking log"""
        result = self.expert.clear_log()
        self.result_label.text = result.replace('=', '').replace('\n\n', '\n')
        # Refresh to show empty log
        self.view_stats(None)


class WelderToolsApp(App):
    """Main Kivy application"""
    
    def build(self):
        # Set window background color
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        # Create screen manager
        sm = ScreenManager()
        
        # Add all screens
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(WeldingSettingsScreen('mig', name='mig'))
        sm.add_widget(WeldingSettingsScreen('tig', name='tig'))
        sm.add_widget(WeldingSettingsScreen('arc', name='arc'))
        sm.add_widget(WireSpeedScreen(name='wire'))
        sm.add_widget(MachineInfoScreen(name='machine'))
        sm.add_widget(MaterialScreen(name='material'))
        sm.add_widget(TrackingScreen(name='tracking'))
        
        return sm


if __name__ == '__main__':
    WelderToolsApp().run()
