from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.config import Config
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
import math

# Window settings
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '1050')
Config.set('graphics', 'resizable', False)

# ============ Physical Constants - FULL VERSION ============
PHYSICS_CONSTANTS = {
    'Quantum Mechanics': {
        'Planck Constant (h)': '6.62607015e-34',
        'Reduced Planck (ħ)': '1.054571817e-34',
        'Planck Length (lP)': '1.616255e-35',
        'Planck Time (tP)': '5.391247e-44',
        'Electron Mass (me)': '9.1093837015e-31',
        'Proton Mass (mp)': '1.67262192369e-27',
        'Neutron Mass (mn)': '1.67492749804e-27',
        'Electron Charge (e)': '1.602176634e-19',
        'Bohr Radius (a₀)': '5.29177210903e-11',
    },
    'Geophysics': {
        'Earth Mass (kg)': '5.9722e24',
        'Earth Radius (m)': '6371000',
        'Surface Gravity (g)': '9.80665',
        'Rotation Period (s)': '86164',
        'Continental Crust (m)': '35000',
        'Oceanic Crust (m)': '7000',
    },
    'Astrophysics': {
        'Speed of Light (c)': '299792458',
        'Gravitational Constant (G)': '6.67430e-11',
        'Hubble Constant (H₀)': '67.4',
        'Age of Universe (years)': '13.8e9',
        'Solar Mass (M☉)': '1.98847e30',
        'Astronomical Unit (AU)': '1.495978707e11',
        'Light Year (ly)': '9.4607304725808e15',
    },
    'Thermodynamics': {
        'Absolute Zero (°C)': '-273.15',
        'Avogadro Number (NA)': '6.02214076e23',
        'Boltzmann Constant (k)': '1.380649e-23',
        'Gas Constant (R)': '8.314462618',
        'Triple Point Water (K)': '273.16',
        'Stefan-Boltzmann (σ)': '5.670374419e-8',
        'Wien Displacement (b)': '2.897771955e-3',
    },
    'Electromagnetism': {
        'Magnetic Constant (μ₀)': '1.25663706212e-6',
        'Electric Constant (ε₀)': '8.8541878128e-12',
        'Coulomb Constant (k)': '8.9875517923e9',
        'Elementary Charge (e)': '1.602176634e-19',
        'Electron Volt (eV)': '1.602176634e-19',
        'Fine Structure (α)': '7.2973525693e-3',
    },
    'Nuclear Physics': {
        'Atomic Mass Unit (u)': '1.66053906660e-27',
        'Fermi (fm)': '1e-15',
        'Rydberg Constant (R∞)': '10973731.568160',
        'Compton Wavelength (λc)': '2.42631023867e-12',
        'Nuclear Magneton (μN)': '5.050783746e-27',
        'Bohr Magneton (μB)': '9.2740100783e-24',
    },
    'Particle Physics': {
        'Muon Mass (mμ)': '1.883531627e-28',
        'Tau Mass (mτ)': '3.16754e-27',
        'W Boson Mass (mW)': '1.433e-25',
        'Z Boson Mass (mZ)': '1.625e-25',
        'Higgs Mass (mH)': '2.235e-25',
    },
    'Relativity': {
        'Schwarzschild Radius': '2GM/c²',
        'Gravitational Time Dilation': '√(1-2GM/rc²)',
        'Lorentz Factor (γ)': '1/√(1-v²/c²)',
        'Minkowski Metric': 'ds² = -c²dt² + dx² + dy² + dz²',
        'Einstein Field Eq': 'G_μν = 8πG T_μν',
    }
}

# ============ Unit Categories ============
UNIT_CATEGORIES = ['Length', 'Mass', 'Time', 'Energy', 'Temperature', 'Area', 'Volume', 'Speed', 'Pressure', 'Force', 'Power']

UNIT_CONVERSIONS = {
    'Length': {
        'Meter': 1.0,
        'Kilometer': 1000.0,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Micrometer': 0.000001,
        'Nanometer': 1e-9,
        'Inch': 0.0254,
        'Foot': 0.3048,
        'Yard': 0.9144,
        'Mile': 1609.344,
        'Nautical Mile': 1852.0,
        'Light Year': 9.461e15,
        'Astronomical Unit': 1.496e11,
    },
    'Mass': {
        'Kilogram': 1.0,
        'Gram': 0.001,
        'Milligram': 0.000001,
        'Microgram': 1e-9,
        'Ton': 1000.0,
        'Pound': 0.45359237,
        'Ounce': 0.0283495,
        'Stone': 6.35029,
        'Solar Mass': 1.98847e30,
    },
    'Time': {
        'Second': 1.0,
        'Millisecond': 0.001,
        'Microsecond': 0.000001,
        'Nanosecond': 1e-9,
        'Minute': 60.0,
        'Hour': 3600.0,
        'Day': 86400.0,
        'Week': 604800.0,
        'Year': 31536000.0,
    },
    'Energy': {
        'Joule': 1.0,
        'Kilojoule': 1000.0,
        'Calorie': 4.184,
        'Kilocalorie': 4184.0,
        'Electron Volt': 1.602176634e-19,
        'Watt Hour': 3600.0,
        'BTU': 1055.06,
        'Erg': 1e-7,
    },
    'Temperature': {
        'Kelvin': 'K',
        'Celsius': 'C',
        'Fahrenheit': 'F',
    },
    'Area': {
        'Square Meter': 1.0,
        'Square Kilometer': 1e6,
        'Square Centimeter': 0.0001,
        'Square Millimeter': 1e-6,
        'Hectare': 10000.0,
        'Acre': 4046.86,
    },
    'Volume': {
        'Cubic Meter': 1.0,
        'Liter': 0.001,
        'Milliliter': 1e-6,
        'Gallon': 0.00378541,
        'Quart': 0.000946353,
    },
    'Speed': {
        'Meter/Second': 1.0,
        'Kilometer/Hour': 0.277778,
        'Mile/Hour': 0.44704,
        'Knot': 0.514444,
        'Speed of Light': 299792458,
    },
    'Pressure': {
        'Pascal': 1.0,
        'Kilopascal': 1000.0,
        'Bar': 100000.0,
        'PSI': 6894.76,
        'Atmosphere': 101325.0,
        'Torr': 133.322,
    },
    'Force': {
        'Newton': 1.0,
        'Kilonewton': 1000.0,
        'Dyne': 1e-5,
        'Pound-force': 4.44822,
    },
    'Power': {
        'Watt': 1.0,
        'Kilowatt': 1000.0,
        'Megawatt': 1e6,
        'Horsepower': 745.7,
    }
}

class CalculatorButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.border = (0, 0, 0, 0)
        self.font_size = dp(18)
        self.bold = True
        
    def on_press(self):
        anim = Animation(opacity=0.7, duration=0.05)
        anim.start(self)
        
    def on_release(self):
        anim = Animation(opacity=1, duration=0.05)
        anim.start(self)

class PhysicsCalculatorApp(App):
    def build(self):
        self.title = "Physics Calculator"
        Window.clearcolor = get_color_from_hex('#0a0c12')
        
        # Calculator state
        self.first_num = None
        self.operation = None
        self.memory = 0
        self.last_result = 0
        self.converter_mode = False
        
        # Main layout
        main_layout = BoxLayout(
            orientation='vertical', 
            spacing=dp(2), 
            padding=dp(5)
        )
        
        # ============ DISPLAY ============
        self.display = TextInput(
            text='0',
            font_size=dp(48),
            halign='right',
            readonly=True,
            multiline=False,
            size_hint=(1, 0.14),
            background_color=get_color_from_hex('#0f1a24'),
            foreground_color=get_color_from_hex('#aaffdd'),
            cursor_color=get_color_from_hex('#aaffdd'),
            
            padding=(dp(15), dp(20))
        )
        main_layout.add_widget(self.display)
        
        # ============ CONVERT TOGGLE ============
        self.convert_toggle = ToggleButton(
            text='CONVERT OFF',
            font_size=dp(13),
            size_hint=(1, 0.04),
            background_normal='',
            background_color=get_color_from_hex('#4a4a4a'),
            color=get_color_from_hex('#ffffff'),
            bold=True,
            state='normal'
        )
        self.convert_toggle.bind(on_press=self.toggle_converter)
        main_layout.add_widget(self.convert_toggle)
        
        # ============ PHYSICAL CONSTANTS ============
        constants_label = Label(
            text='PHYSICAL CONSTANTS',
            size_hint=(1, 0.03),
            color=get_color_from_hex('#88aaff'),
            font_size=dp(16),
            bold=True,
            halign='center'
        )
        main_layout.add_widget(constants_label)
        
        # Constants spinners
        constants_frame = BoxLayout(size_hint=(1, 0.10), spacing=dp(5))
        
        # Field spinner
        self.field_spinner = Spinner(
            text='Quantum Mechanics',
            values=list(PHYSICS_CONSTANTS.keys()),
            size_hint=(0.5, 1),
            background_color=get_color_from_hex('#1e3a5a'),
            color=get_color_from_hex('#ffffff'),
            font_size=dp(14),
            height=dp(40),
            bold=True
        )
        self.field_spinner.bind(text=self.on_field_change)
        
        # Constant spinner
        self.constant_spinner = Spinner(
            text='Planck Constant (h)',
            values=self.get_constant_list('Quantum Mechanics'),
            size_hint=(0.5, 1),
            background_color=get_color_from_hex('#2a4a6a'),
            color=get_color_from_hex('#ffffff'),
            font_size=dp(13),
            height=dp(40),
            bold=True
        )
        self.constant_spinner.bind(text=self.on_constant_change)
        
        constants_frame.add_widget(self.field_spinner)
        constants_frame.add_widget(self.constant_spinner)
        main_layout.add_widget(constants_frame)
        
        # ============ UNIT CONVERTER ============
        self.converter_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.18))
        self.converter_layout.opacity = 0
        self.converter_layout.disabled = True
        
        converter_label = Label(
            text='UNIT CONVERTER',
            size_hint=(1, 0.08),
            color=get_color_from_hex('#aaffaa'),
            font_size=dp(14),
            bold=True,
            halign='center'
        )
        self.converter_layout.add_widget(converter_label)
        
        # Category spinner
        self.unit_category_spinner = Spinner(
            text='Length',
            values=UNIT_CATEGORIES,
            size_hint=(1, 0.16),
            background_color=get_color_from_hex('#2a5a4a'),
            color=get_color_from_hex('#ffffff'),
            font_size=dp(12),
            height=dp(35)
        )
        self.unit_category_spinner.bind(text=self.on_unit_category_change)
        self.converter_layout.add_widget(self.unit_category_spinner)
        
        # From and To units frame
        units_frame = BoxLayout(size_hint=(1, 0.30), spacing=dp(10))
        
        initial_units = self.get_unit_list('Length')
        
        # From spinner
        self.from_unit_spinner = Spinner(
            text='Meter',
            values=initial_units,
            size_hint=(0.5, 1),
            background_color=get_color_from_hex('#3a6a5a'),
            color=get_color_from_hex('#ffffff'),
            font_size=dp(14),
            height=dp(40),
            bold=True
        )
        self.from_unit_spinner.bind(text=self.on_conversion_change)
        
        # To spinner
        self.to_unit_spinner = Spinner(
            text='Kilometer',
            values=initial_units,
            size_hint=(0.5, 1),
            background_color=get_color_from_hex('#3a6a5a'),
            color=get_color_from_hex('#ffffff'),
            font_size=dp(14),
            height=dp(40),
            bold=True
        )
        self.to_unit_spinner.bind(text=self.on_conversion_change)
        
        units_frame.add_widget(self.from_unit_spinner)
        units_frame.add_widget(self.to_unit_spinner)
        self.converter_layout.add_widget(units_frame)
        
        # Convert Now Button
        convert_btn = CalculatorButton(
            text='CONVERT',
            font_size=dp(13),
            size_hint=(1, 0.14),
            background_color=get_color_from_hex('#4a8a6a'),
            color=get_color_from_hex('#ffffff'),
            bold=True
        )
        convert_btn.bind(on_press=self.convert_value)
        self.converter_layout.add_widget(convert_btn)
        
        main_layout.add_widget(self.converter_layout)
        
        # ============ SCIENTIFIC FUNCTIONS ============
        sci_label = Label(
            text='SCIENTIFIC FUNCTIONS',
            size_hint=(1, 0.02),
            color=get_color_from_hex('#aaddff'),
            font_size=dp(14),
            bold=True,
            halign='center'
        )
        main_layout.add_widget(sci_label)
        
        # Scientific buttons grid
        sci_grid = GridLayout(cols=6, spacing=dp(1), size_hint=(1, 0.11))
        
        sci_buttons = [
            'sin', 'cos', 'tan', 'log', 'ln', '10^x',
            'x²', 'x³', 'x^y', '√', '∛', 'e^x',
            'π', 'e', 'n!', '1/x', '|x|', 'mod',
        ]
        
        for func in sci_buttons:
            btn = CalculatorButton(
                text=func,
                font_size=dp(12),
                background_color=get_color_from_hex('#2a4a6a'),
                color=get_color_from_hex('#ffffff')
            )
            btn.bind(on_press=self.on_scientific)
            sci_grid.add_widget(btn)
        
        main_layout.add_widget(sci_grid)
        
        # ============ KEYPAD ============
        keypad = GridLayout(cols=5, spacing=dp(2), size_hint=(1, 0.25))
        
        keypad_buttons = [
            'C', '⌫', '÷', '×', '−',
            '7', '8', '9', '+', '(',
            '4', '5', '6', '-', ')',
            '1', '2', '3', 'EXP', 'ANS',
            '0', '00', '.', '±', '=',
        ]
        
        for btn_text in keypad_buttons:
            if btn_text in ['C', '⌫', '±']:
                color = '#8a2a2a'
                font_size = dp(20)
            elif btn_text in ['÷', '×', '−', '+', '=']:
                color = '#b85e00'
                font_size = dp(22)
            elif btn_text in ['(', ')']:
                color = '#2a5a5a'
                font_size = dp(20)
            elif btn_text in ['EXP', 'ANS']:
                color = '#2a5a7a'
                font_size = dp(18)
            elif btn_text.isdigit() or btn_text == '00' or btn_text == '0':
                color = '#2a3a4a'
                font_size = dp(26)
            elif btn_text == '.':
                color = '#2a3a4a'
                font_size = dp(26)
            else:
                color = '#2a3a4a'
                font_size = dp(20)
            
            btn = CalculatorButton(
                text=btn_text,
                font_size=font_size,
                background_color=get_color_from_hex(color),
                color=get_color_from_hex('#ffffff')
            )
            btn.bind(on_press=self.on_button_press)
            keypad.add_widget(btn)
        
        main_layout.add_widget(keypad)
        
        # ============ MEMORY BUTTONS ============
        memory_label = Label(
            text='MEMORY FUNCTIONS',
            size_hint=(1, 0.02),
            color=get_color_from_hex('#cc99ff'),
            font_size=dp(13),
            bold=True,
            halign='center'
        )
        main_layout.add_widget(memory_label)
        
        memory_layout = GridLayout(cols=5, spacing=dp(2), size_hint=(1, 0.05))
        memory_buttons = ['MC', 'MR', 'M+', 'M-', 'MS']
        for mem in memory_buttons:
            btn = CalculatorButton(
                text=mem,
                font_size=dp(14),
                background_color=get_color_from_hex('#4a2a5a'),
                color=get_color_from_hex('#ffffff')
            )
            btn.bind(on_press=self.on_memory)
            memory_layout.add_widget(btn)
        main_layout.add_widget(memory_layout)
        
        return main_layout
    
    def toggle_converter(self, instance):
        """Toggle unit converter on/off"""
        if self.converter_mode:
            self.converter_mode = False
            self.convert_toggle.text = 'CONVERT OFF'
            self.convert_toggle.background_color = get_color_from_hex('#4a4a4a')
            self.converter_layout.opacity = 0
            self.converter_layout.disabled = True
        else:
            self.converter_mode = True
            self.convert_toggle.text = 'CONVERT ON'
            self.convert_toggle.background_color = get_color_from_hex('#4a8a6a')
            self.converter_layout.opacity = 1
            self.converter_layout.disabled = False
    
    def get_unit_list(self, category):
        """Get list of units for a category"""
        if category in UNIT_CONVERSIONS:
            return list(UNIT_CONVERSIONS[category].keys())
        return []
    
    def on_unit_category_change(self, spinner, text):
        """When unit category changes"""
        units = self.get_unit_list(text)
        self.from_unit_spinner.values = units
        self.to_unit_spinner.values = units
        if len(units) > 0:
            self.from_unit_spinner.text = units[0]
            if len(units) > 1:
                self.to_unit_spinner.text = units[1]
            else:
                self.to_unit_spinner.text = units[0]
    
    def on_conversion_change(self, spinner, text):
        """When unit changes"""
        pass
    
    def convert_value(self, instance=None):
        """Convert the displayed value"""
        if not self.converter_mode:
            return
        
        try:
            if self.display.text in ['Error', '']:
                return
            
            value = float(self.display.text)
            category = self.unit_category_spinner.text
            from_unit = self.from_unit_spinner.text
            to_unit = self.to_unit_spinner.text
            
            if category and from_unit and to_unit and category in UNIT_CONVERSIONS:
                if category == 'Temperature':
                    result = self.convert_temperature(value, from_unit, to_unit)
                else:
                    base_value = value * UNIT_CONVERSIONS[category][from_unit]
                    result = base_value / UNIT_CONVERSIONS[category][to_unit]
                
                self.display.text = self.format_number(result)
                
        except Exception as e:
            print(f"Conversion error: {e}")
    
    def convert_temperature(self, value, from_unit, to_unit):
        """Convert temperature"""
        if from_unit == 'Kelvin':
            celsius = value - 273.15
        elif from_unit == 'Celsius':
            celsius = value
        elif from_unit == 'Fahrenheit':
            celsius = (value - 32) * 5/9
        else:
            celsius = value
        
        if to_unit == 'Kelvin':
            return celsius + 273.15
        elif to_unit == 'Celsius':
            return celsius
        elif to_unit == 'Fahrenheit':
            return celsius * 9/5 + 32
        else:
            return celsius
    
    def get_constant_list(self, field):
        """Format constants list - عرض الأسماء الكاملة"""
        if field in PHYSICS_CONSTANTS:
            constants = PHYSICS_CONSTANTS[field]
            formatted_list = []
            for name, value in constants.items():
                formatted_list.append(f"{name}")
            return formatted_list
        return []
    
    def on_field_change(self, spinner, text):
        """When physics field changes"""
        constants = self.get_constant_list(text)
        self.constant_spinner.values = constants
        if constants:
            self.constant_spinner.text = constants[0]
            if text in PHYSICS_CONSTANTS and constants[0]:
                for full_name, value in PHYSICS_CONSTANTS[text].items():
                    if full_name == constants[0]:
                        self.display.text = value
                        break
    
    def on_constant_change(self, spinner, text):
        """When constant is selected"""
        try:
            if text:
                field = self.field_spinner.text
                if field in PHYSICS_CONSTANTS:
                    for full_name, value in PHYSICS_CONSTANTS[field].items():
                        if full_name == text:
                            self.display.text = value
                            break
        except:
            pass
    
    def on_scientific(self, instance):
        """Scientific functions"""
        func = instance.text
        try:
            if self.display.text in ['Error', '']:
                self.display.text = '0'
            
            value = float(self.display.text)
            
            if func == 'sin':
                result = math.sin(math.radians(value))
            elif func == 'cos':
                result = math.cos(math.radians(value))
            elif func == 'tan':
                result = math.tan(math.radians(value))
            elif func == 'log':
                result = math.log10(value) if value > 0 else 'Error'
            elif func == 'ln':
                result = math.log(value) if value > 0 else 'Error'
            elif func == '10^x':
                result = 10 ** value
            elif func == 'x²':
                result = value ** 2
            elif func == 'x³':
                result = value ** 3
            elif func == 'x^y':
                self.first_num = value
                self.operation = '^'
                self.display.text = '0'
                return
            elif func == '√':
                result = math.sqrt(value) if value >= 0 else 'Error'
            elif func == '∛':
                result = value ** (1/3) if value >= 0 else -((-value) ** (1/3))
            elif func == 'e^x':
                result = math.exp(value)
            elif func == 'π':
                result = math.pi
            elif func == 'e':
                result = math.e
            elif func == 'n!':
                if value >= 0 and value == int(value) and value <= 170:
                    result = math.factorial(int(value))
                else:
                    result = 'Error'
            elif func == '1/x':
                result = 1 / value if value != 0 else 'Error'
            elif func == '|x|':
                result = abs(value)
            elif func == 'mod':
                self.first_num = value
                self.operation = 'mod'
                self.display.text = '0'
                return
            
            if result == 'Error':
                self.display.text = 'Error'
            else:
                self.display.text = self.format_number(result)
                self.last_result = result
                
        except:
            self.display.text = 'Error'
    
    def on_memory(self, instance):
        """Memory operations"""
        op = instance.text
        try:
            current = float(self.display.text) if self.display.text not in ['0', 'Error', ''] else 0
            
            if op == 'MC':
                self.memory = 0
            elif op == 'MR':
                self.display.text = str(self.memory)
            elif op == 'M+':
                self.memory += current
            elif op == 'M-':
                self.memory -= current
            elif op == 'MS':
                self.memory = current
        except:
            pass
    
    def on_button_press(self, instance):
        """Basic button operations"""
        text = instance.text
        
        try:
            if text == 'C':
                self.display.text = '0'
                self.first_num = None
                self.operation = None
            elif text == '⌫':
                current = self.display.text
                if len(current) > 1 and current != 'Error':
                    self.display.text = current[:-1]
                else:
                    self.display.text = '0'
            elif text == '=':
                self.calculate()
            elif text == 'ANS':
                self.display.text = str(self.last_result) if self.last_result != 0 else '0'
            elif text == 'EXP':
                current = self.display.text
                if current != 'Error' and 'e' not in current:
                    self.display.text = current + 'e'
            elif text == '±':
                current = self.display.text
                if current not in ['0', 'Error']:
                    if current.startswith('-'):
                        self.display.text = current[1:]
                    else:
                        self.display.text = '-' + current
            elif text == '.':
                current = self.display.text
                if current == 'Error':
                    self.display.text = '0.'
                elif '.' not in current:
                    self.display.text = current + '.'
            elif text == '(':
                self.display.text += '('
            elif text == ')':
                self.display.text += ')'
            elif text == '00':
                current = self.display.text
                if current != '0' and current != 'Error':
                    self.display.text = current + '00'
                else:
                    self.display.text = '0'
            elif text in ['÷', '×', '−', '+']:
                if self.display.text not in ['Error', '']:
                    self.first_num = float(self.display.text)
                    if text == '÷':
                        self.operation = '/'
                    elif text == '×':
                        self.operation = '*'
                    elif text == '−':
                        self.operation = '-'
                    else:
                        self.operation = '+'
                    self.display.text = '0'
            elif text.isdigit():
                current = self.display.text
                if current == '0' or current == 'Error' or current == '':
                    self.display.text = text
                else:
                    self.display.text = current + text
                
        except:
            self.display.text = 'Error'
    
    def calculate(self):
        """Calculate result"""
        if self.first_num is not None and self.operation:
            try:
                second_num = float(self.display.text)
                
                if self.operation == '+':
                    result = self.first_num + second_num
                elif self.operation == '-':
                    result = self.first_num - second_num
                elif self.operation == '*':
                    result = self.first_num * second_num
                elif self.operation == '/':
                    if second_num != 0:
                        result = self.first_num / second_num
                    else:
                        result = 'Error'
                elif self.operation == '^':
                    result = self.first_num ** second_num
                elif self.operation == 'mod':
                    result = self.first_num % second_num
                else:
                    result = 'Error'
                
                if result == 'Error':
                    self.display.text = 'Error'
                else:
                    self.display.text = self.format_number(result)
                    self.last_result = result
                
                self.first_num = None
                self.operation = None
                
            except:
                self.display.text = 'Error'
    
    def format_number(self, num):
        """Format number"""
        if isinstance(num, float):
            if abs(num) >= 1e10 or (abs(num) <= 1e-10 and num != 0):
                return f"{num:.6e}"
            elif num.is_integer():
                return str(int(num))
            else:
                rounded = round(num, 8)
                if rounded.is_integer():
                    return str(int(rounded))
                else:
                    s = f"{rounded:.8f}".rstrip('0').rstrip('.')
                    return s
        return str(num)

if __name__ == '__main__':
    PhysicsCalculatorApp().run()