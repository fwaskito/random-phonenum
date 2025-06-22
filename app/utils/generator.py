# Created Date: Sat, Jun 21th 2025
# Author: F. Waskito
# Last Modified: Sat, Jun 21th 2025 22:53:57 PM

import random


class RandomNumberGenerator:
    def __init__(
        self,
        n: int,
        prefix: str = "",
        duplicate_amount: float = 0.0,
    ) -> None:
        self._n = n
        self._prefix = prefix
        self._duplicate_amount = duplicate_amount
        self.distribution = {}
        self.phone_numbers = []

    """
        Getting a cellular number prefix.

    A prefix of cellular number is the first four in cellular number
    that registred as Indonesian phone number provider code. In this 
    list of context, the prefix without a leading '0' (zero).

    Returns:
        int: three numbers of cellular provider code

    Reference:
    - https://id.wikipedia.org/wiki/Nomor_telepon_di_Indonesia
    """

    def _get_cell_num_codes(self, idx: int):
        cell_num_codes = {
            0: "811",  # Telkomsel  | Telkomsel Halo
            1: "812",  # Telkomsel  | Telkomsel Halo & SIMPATI
            2: "813",  # Telkomsel  | Telkomsel Halo & SIMPATI
            3: "814",  # Indosat    | IM3 Prabayar
            4: "815",  # Indosat    | IM3 Prabayar & Platinum
            5: "816",  # Indosat    | IM3 Prabayar & Platinum
            6: "817",  # XL SMART   | XL Prabayar & prioritas
            7: "818",  # XL SMART   | XL Prabayar & prioritas
            8: "819",  # XL SMART   | XL Prabayar & prioritas
            9: "821",  # Telkomsel  | SIMPATI
            10: "822",  # Telkomsel | SIMPATI
            11: "823",  # Telkomsel | SIMPATI
            12: "831",  # XL SMART  | AXIS
            13: "832",  # XL SMART  | AXIS
            14: "833",  # XL SMART  | AXIS
            15: "838",  # XL SMART  | AXIS
            16: "851",  # Telkomsel | SIMPATI & by U
            17: "852",  # Telkomsel | SIMPATI
            18: "853",  # Telkomsel | SIMPATI
            19: "855",  # Indosat   | IM3 Prabayar & Platinum
            20: "856",  # Indosat   | IM3 Prabayar
            21: "857",  # Indosat   | IM3 Prabayar
            22: "858",  # Indosat   | IM3 Prabayar
            23: "868",  # PSN/ACes
            24: "877",  # XL SMART  | XL Prabayar
            25: "878",  # XL SMART  | XL Prabayar
            26: "879",  # XL SMART  | XL Prabayar
            27: "881",  # XL SMART  | Smartfren
            28: "882",  # XL SMART  | Smartfren
            29: "883",  # XL SMART  | Smartfren
            30: "884",  # XL SMART  | Smartfren
            31: "885",  # XL SMART  | Smartfren
            32: "886",  # XL SMART  | Smartfren
            33: "887",  # XL SMART  | Smartfren
            34: "888",  # XL SMART  | Smartfren
            35: "889",  # XL SMART  | Smartfren
            36: "895",  # Indosat   | 3
            37: "896",  # Indosat   | 3
            38: "897",  # Indosat   | 3
            39: "898",  # Indosat   | 3
            40: "899",  # Indosat   | 3
        }

        return cell_num_codes[idx]

    def generate(self):
        phone_number_set = set()
        n_uniques = self._n - (self._n * self._duplicate_amount)
        while len(phone_number_set) < n_uniques:
            phone_number = self._prefix
            # Indonesian cellular provider code
            phone_number += self._get_cell_num_codes(random.randint(0, 40))

            # the other 8 numbers can be in the range of 0 to 9.
            for _ in range(8):
                phone_number += str(random.randint(0, 9))

            phone_number_set.add(phone_number)

        self.distribution["unique"] = len(phone_number_set)
        self.phone_numbers = list(phone_number_set)

        i = 0
        while len(self.phone_numbers) < self._n:
            phone_number = self.phone_numbers[i]
            self.phone_numbers.append(phone_number)
            i += 1

        self.distribution["duplicate"] = i
        self.distribution["total"] = len(self.phone_numbers)
