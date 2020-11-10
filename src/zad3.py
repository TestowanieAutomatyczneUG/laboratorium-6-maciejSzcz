import math
import unittest


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


class StatementTest(unittest.TestCase):
    def test_statement_comedy_audience_lt_20(self):
        self.assertEqual(statement({"customer": "random", "performances": [{"playID": "as-like", "audience": 19}]}, {"as-like": {"name": "As You Like It", "type": "comedy"}}), "Statement for random\n As You Like It: $357.00 (19 seats)\nAmount owed is $357.00\nYou earned 3 credits\n")

    def test_statement_comedy_audience_gt_20(self):
        self.assertEqual(statement({"customer": "random", "performances": [{"playID": "as-like", "audience": 24}]}, {"as-like": {"name": "As You Like It", "type": "comedy"}}), "Statement for random\n As You Like It: $492.00 (24 seats)\nAmount owed is $492.00\nYou earned 4 credits\n")

    def test_statement_tragedy_audience_lt_30(self):
        self.assertEqual(statement({"customer": "random", "performances": [{"playID": "othello", "audience": 11}]}, {"othello": {"name": "Othello", "type": "tragedy"}}), "Statement for random\n Othello: $400.00 (11 seats)\nAmount owed is $400.00\nYou earned 0 credits\n")

    def test_statement_tragedy_audience_gt_30(self):
        self.assertEqual(statement({"customer": "random", "performances": [{"playID": "othello", "audience": 51}]}, {"othello": {"name": "Othello", "type": "tragedy"}}), "Statement for random\n Othello: $610.00 (51 seats)\nAmount owed is $610.00\nYou earned 21 credits\n")

    def test_statement_unknown_type_error(self):
        self.assertRaises(ValueError, statement, {"customer": "random", "performances": [{"playID": "hamlet", "audience": 1}]}, {"hamlet": {"name": "Hamlet", "type": "action"}})

    def test_statement_no_performances(self):
        self.assertEqual("Statement for random\nAmount owed is $0.00\nYou earned 0 credits\n", statement({"customer": "random", "performances": []}, {}))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
