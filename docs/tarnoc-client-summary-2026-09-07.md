# Tarnoc financial model: what it is and what it says

Version of 7 September 2026. All figures in euros. Monthly model, January 2026
to December 2030. The 2026 numbers are the committed plan and are held fixed.

---

## 1. What this model is

It is a full monthly operating model for Tarnoc: profit and loss, balance sheet
and cash flow, driven off a single Assumptions tab.

The important design choice is this: **units sold and headcount are not typed
in. They are calculated.** In most plans, somebody types "we will sell 5,000
units in 2029" and the rest of the spreadsheet does arithmetic on that
assertion. Here you set the drivers, marketing spend, how many sales people you
hire, how many installer partners you sign, how much the assembly partner can
build, and the model works out how many units that actually produces. If the
plan cannot support the volume, the volume comes down on its own.

There are two versions of the workbook, one for each funding case, so nobody has
to work a switch:

- **Base case**, a EUR3m raise.
- **Aggressive case**, a EUR10m raise with money going into own manufacturing.

---

## 2. What you type in

Every number you can change sits on the Assumptions tab. The main ones:

**Products and price.** Turbineketel EUR8,526, Combi+ EUR13,836, sold 20/80.
Installation is passed through at cost. Service contracts run on the installed
base at 88% attach, EUR60 to EUR200 a year.

**Cost of a unit.** The bill of materials falls with volume in three steps:
EUR9,984 below 5,000 units, EUR7,069 from 5,000, EUR4,998 from 10,000. The step
is set on this year plus next year's volume, which assumes the supplier prices
on a two-year commitment. On top of the BOM sit the outdoor unit, shipping,
service parts and a 10% commission to the installer on channel sales.

**Demand.** Marketing spend, EUR120 per lead, half of leads qualified, 40% of
those won. Plus orders that installer partners bring in themselves, one a month
each in 2027 rising to four by 2030.

**Selling capacity.** Sales reps sell 20 units a month. Installer partners sell
8. The share sold direct falls from 80% in 2027 to 30% in 2030 as the partner
channel takes over.

**Build capacity.** The assembly partner can build 650 a month in the base case
and 1,000 in the aggressive case. In the aggressive case, two automated
production lines add 1,000 a month each.

**People.** Almost all roles are sized by a ratio: support staff per installed
unit, field engineers one per 600 units on contract, trainers per partner
signed, line operators 25 per line. Only R&D hires and the back office are typed
in by year.

**Money.** The raise, its date, working capital terms (20 days to collect, 45
days to pay, no stock), wage inflation 5% a year, other costs 10%.

---

## 3. How the model decides how many units get sold

Each month it works out three numbers and takes **the smallest**:

1. How many customers the marketing spend and the partner network produce.
2. How many the sales team and the partners can physically sell.
3. How many the factory and the assembly partner can build.

Nothing is sold before January 2027, because there is nothing sellable before
then. This is the answer to the question every investor asks, which is "where
does the volume come from". It comes from spend and people, and it stops when
one of the three runs out.

---

## 4. What comes out

|  | Base, EUR3m | Aggressive, EUR10m |
| --- | --- | --- |
| Units 2027 | 354 | 2,812 |
| Units 2028 | 1,344 | 6,864 |
| Units 2029 | 4,122 | 11,730 |
| Units 2030 | 7,407 | 18,780 |
| Installed base end 2030 | 13,227 | 40,186 |
| Revenue 2027 | EUR6.0m | EUR47.6m |
| Revenue 2030 | EUR126.3m | EUR321.1m |
| Gross margin 2027 / 2030 | 10% / 37% | 28% / 37% |
| EBITDA 2027 | -EUR2.5m | +EUR4.8m |
| EBITDA 2028 | +EUR0.9m | +EUR22.8m |
| EBITDA 2030 | +EUR33.6m | +EUR78.6m |
| Headcount end 2030 | 95 | 302 |
| Capital expenditure | none | EUR9.0m, lines and tooling |
| Lowest cash after the raise | EUR0.60m, Dec 2027 | EUR0.99m, Jan 2027 |
| Months of cost that covers | 2.3 | 1.4 |
| Share of the raise the plan uses | 80% | 90% |
| Cash end 2030 | EUR42.9m | EUR122.7m |

---

## 5. What the numbers mean

Gross margin is set by the BOM volume tier: about 10% below 5,000 units, 25%
from 5,000, 37% from 10,000. Almost all the profit in both cases comes from
moving down those tiers. We tested eight other levers on 7 September and none
changed the outcome by a comparable amount.

The base case becomes profitable in 2028 at EUR0.9m EBITDA. It gets there
because 2028 and 2029 volume together is 5,466 units, which clears the 5,000
threshold and puts 2028 on the EUR7,069 BOM. That is a margin of 466 units,
about 9%. If combined volume falls below 5,000, 2028 costs about EUR2,900 more
per unit, EBITDA is about minus EUR3m, and cash goes negative.

The base plan uses 80% of the EUR3m and never falls below EUR0.60m, which is
2.3 months of running costs at the low point in December 2027.

The aggressive case is profitable in its first selling year: EUR4.8m EBITDA on
2,812 units in 2027, because two-year volume pricing puts 2027 onto the second
BOM tier. Investors will question this without a supplier contract.

The aggressive case spends EUR9m on production lines that produce no cost
saving in the model. The BOM is charged in full whoever assembles the unit,
because we do not know what the assembly partner charges. The lines add capacity
and the plan uses about half of it by 2030. The argument for building is
therefore control and independence from a single supplier, not cost, until the
client gives us the partner's fee.

The aggressive case is tight at the start. It uses 90% of the EUR10m and the low
point is EUR0.99m in January 2027, 1.4 months of running costs, immediately
after the capex and in the first month of sales. Deploying 90% of the raise and
holding two to three months of cover cannot both hold at EUR10m.

## 6. Where the plan is most exposed

1. **The BOM cost-down from EUR9,984 to EUR4,998, a 50% fall.** Published
   learning-curve evidence for heat pumps supports about 30%. There is no
   supplier quote behind it yet. Everything in both cases rests on this number.
2. **Two-year volume pricing.** Without it, 2027 and 2028 are priced at the top
   step, both cases lose a year of margin, and the base case does not close on
   EUR3m.
3. **The turbineketel sells below its first-step BOM.** At EUR8,526 against
   EUR9,984, every early turbineketel loses money before commission. Volume
   fixes it. A price cut makes it worse.
4. **Sales productivity of 20 units per rep per month.** Comparable HVAC and
   solar businesses run 6 to 10. This matters most in 2027 and 2028.
5. **Service attach at 88%.** Market data shows about 76% of new buyers hold a
   contract.
6. **The channel shift.** Selling 30% direct by 2030 needs 113 active installer
   partners in the base case and 277 in the aggressive one.
7. **No warranty reserve** beyond the 3% inside the BOM. Comparable companies
   carry 1.5 to 3.5% of revenue.
8. **Revenue per person reaches EUR1.1m to EUR1.3m.** Established manufacturers
   run EUR200k to EUR330k. Outsourced assembly and pass-through installation
   explain part of the gap, not all of it.

---

## 7. What we need from you

1. Supplier quotes behind the three BOM steps, and confirmation that the
   supplier will price on a two-year volume commitment.
2. What the assembly partner charges per unit, and whether that fee sits inside
   the BOM figures.
3. Confirmation of the installer deal: 10% of the unit price, on top of the
   installation fee.
4. A view on the shift from direct selling to installers, and on 18,800 units by
   2030 in the aggressive case.
5. A decision on the aggressive raise: EUR10m with six weeks of cover, or
   EUR11m to EUR12m with two to three months.

---

## 8. What has been checked

Every formula in both workbooks has been checked four ways. The model is
recalculated end to end and compared, cell by cell, against a completely
separate re-implementation of the same logic written in Python. The balance
sheet ties in all sixty months. Sources equal uses. Funding received equals the
funding typed in. Every cross-tab link lands where it should.

On top of that the audit now tests whether the answers are possible in the real
world, not only whether the formulas agree with each other, and it does so at
4,000 different sets of inputs rather than only at the numbers as they stand
today. It requires people,
partners, production lines and units to be whole numbers, headcount never to go
backwards, cash never to go below zero, revenue per unit to look like the
product, tax never to exceed the statutory rate, and the installed base to equal
everything sold. Two independent line-by-line reviews on 7 September found about
twenty defects, and these reality checks then found two more. All were fixed and
re-checked. The 2026 committed plan reconciles to your own model to the euro.

What none of this settles is whether the assumptions are right. A 50% reduction
in the bill of materials is either achievable or it is not, and only a supplier
quote will tell us. The checks prove the model does what it says with the numbers
it is given.

The model has no formula errors and no hardcoded results. Change any assumption
and every number downstream moves.
