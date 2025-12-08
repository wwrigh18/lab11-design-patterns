from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    
    def operate(self, text: str = None) -> str:
        """:return: capital letters separated by a period and a space"""
        words = text.split(" ")
        initials = []
        for x in words:
            if len(x) != 0:
                initials.append(x[0])

        str = ""
        for i in range(len(initials)):
            str += (initials[i] + ".")
            if i < len(initials) - 1:
                str += " "
        
        return str

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize