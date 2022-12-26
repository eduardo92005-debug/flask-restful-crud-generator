from mako.template import Template

class ModelGenerator:
    def __init__(self, model_name, tablename):
        self.NO_MATCH = "NO_MATCH"
        self.__tablename = tablename
        self.__model_name = model_name
        self.__model_attributes = []
        self.__auto_increment = False
        self.__is_primary_key = False
        self.__modifier = []
        self.__unique = False
        self.__nullable = False
        self.__model_attribute_name = None
        self.__model_attribute_type = None
        self.__available_types = ['String', 'Integer', 'Float', 'Boolean', 'Date', 'Datetime']
        self.__columns = True

    def add_attribute(self, string):
        self.__model_attributes.append(string)
        return self

    def matcher(self, command):
        match command:
            case "y" | "Y" | "yes" | "Yes" | "YES":
                return self
            case _:
                return None

    
    def handler(self):
        self.__model_attribute_name = input("Enter the name of the attribute: ")
        self.__model_attribute_type = input("Enter the type of the attribute: ")
        if self.__model_attribute_type not in self.__available_types:
            print("Invalid type")
            return
        self.__auto_increment = input("Is this attribute auto increment? (y/n): ")
        if(self.matcher(self.__auto_increment) is not None):
            self.matcher(self.__auto_increment).add_attribute('autoincrement=True').__auto_increment = True
        self.__is_primary_key = input("Is this attribute the primary key? (y/n): ")
        if(self.matcher(self.__is_primary_key) is not None):
            self.matcher(self.__is_primary_key).add_attribute('primary_key=True').__is_primary_key = True
        self.__unique = input("Is this attribute unique? (y/n): ")
        if(self.matcher(self.__unique) is not None):
            self.matcher(self.__unique).add_attribute('unique=True').__unique = True
        self.__nullable = input("Is this attribute nullable? (y/n): ")
        if(self.matcher(self.__nullable) is not None):
            self.matcher(self.__nullable).add_attribute('nullable=True').__nullable = True
        has_modifier = input("Do you want add new modifier? Like default, foreign key... (y/n): ")
        if(has_modifier):
            while True:
                in_modifier = input("Enter the modifier: ")
                self.__modifier.append(in_modifier)
                has_modifier = input("Do you want add new modifier? Like default, foreign key... (y/n): ")
                if not in_modifier:
                    break

    def generate(self):
        template = Template(filename='./src/templates/model_template.py.mako')
        return template.render(model_name=self.__model_name, 
                                tablename=self.__tablename,
                                attr_name=self.__model_attribute_name, 
                                attr_type=self.__model_attribute_type,
                                attr_args=self.__model_attributes)

    @property
    def model_attributes(self):
        return self.__model_attributes