from app.helper.descriptor_helper import Descriptors


class HelpView:
    descriptors = Descriptors

    @classmethod
    def display(cls) -> None:
        """
        Just a bunch of string formatting for displaying a help menu showcasing an ID, the collector's names,
        CLI arguments and function parameters (in that order).
        """
        id_field_len, name_field_len, cmd_field_len, parameter_field_len = (
            3,
            30,
            22,
            20,
        )  # Description field just takes up whatever it needs - we do not assume any 80 char line width
        print(
            f"{'#':<{id_field_len}} {'Collector':<{name_field_len}}{'Shell Long Option':<{cmd_field_len}}{'Instance Parameter':<{parameter_field_len}}"
        )
        print("-" * (id_field_len + name_field_len + cmd_field_len + parameter_field_len))
        for idx, category in enumerate(cls.descriptors.get_all_categories(), start=1):
            id_field = f"{str(idx) + '.':<{id_field_len}}"
            name_field = f"{category.name:<{name_field_len}}"
            cmd_field = f"{category.cmd_arg:<{cmd_field_len}}"
            parameter_field = f"{category.parameter + '=True':<{parameter_field_len}}"
            # description_field = f"{category[3]}"
            print(f"{id_field} {name_field}{cmd_field}{parameter_field}")

            """For some reason enumerate doesn't reset it's (idy) counter
            when finishing the inner loop and starting over, so we do it the old way"""
            idy = 0
            for module in cls.descriptors.get_all_descriptors():  # O^2 but whatever ...
                if module.category.name == category.name:
                    idy += 1
                    _id_field = f"{str(idx) + '.' + str(idy):<{id_field_len}}"
                    _name_field = f"{module.name:<{name_field_len}}"
                    _cmd_field = f"{module.cmd_arg:<{cmd_field_len}}"
                    _parameter_field = f"{module.parameter + '=True':<{parameter_field_len}}"
                    # _description_field = f"{module.description}"
                    print(f"{_id_field} {_name_field}{_cmd_field}{_parameter_field}")
            print()


if __name__ == "__main__":
    HelpView.display()
