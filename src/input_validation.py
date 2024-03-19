from typing import Optional

class InputValidation:
    @staticmethod
    def input_number_validation(prompt_message: str, expected_type: Optional[str] = "numerik",
                                lower_bound: Optional[float] = float('-inf'), upper_bound: Optional[float] = float('inf')):
        input_valid = False
        while not input_valid:
            input_number = input(prompt_message)
            if not InputValidation.is_input_type_valid(input_number, expected_type):
                print(f"Input harus berupa angka {expected_type}!")
            elif float(input_number) >= lower_bound and float(input_number) <= upper_bound:
                input_valid = True
            else:
                if lower_bound == float('-inf'):
                    print(f"Angka harus kurang dari sama dengan {upper_bound}!")
                elif upper_bound == float('inf'):
                    print(f"Angka harus lebih dari sama dengan {lower_bound}!")
                else:
                    print(f"Angka harus antara {lower_bound} sampai {upper_bound}!")
        
        return input_number

    @staticmethod
    def is_input_type_valid(input_number: object, expected_type: str):
        try:
            if expected_type == "integer":
                return isinstance(int(input_number), int)
            else:
                return isinstance(float(input_number), (int,float))
            
        except ValueError:
            return False