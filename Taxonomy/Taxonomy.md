# KPI Taxonomy

The idea is to divide the various KPIs in differents classes of distinct Nature, so that it can be useful to understand better the KPIs, know where to look if you need something specific, and where to add new KPIs in a scalable scenario.

To better explain every KPIs, we are going to define some catch all words.

**_machine_** will define a singular machine. The machine depends on the system.

**_metric_** will define a metric used by that specific KPI. We are currently using:
- **average**
- **max**
- **min**
- **sum**

**_timeframe_** will define a timeframe where are we going to calculate the metric. We are currently using:
- **daily**
- **last_day**
- **weekly**
- **last_week**
- **monthly**
- **last_month**
- **yearly**
- **last_year**

Every timeframe also has a last_ counterpart because we really need a recency control to catch up errors and patterns the moment they appears.

## Time KPIs

The Time KPIs serve the purpose of checking the various machines in the time axis.

- ***metric*_*timeframe*_working_time**: The amount of time the machine has been online
- ***metric*_*timeframe*_idle_time**: The amount of time the machine has been idle
- ***metric*_*timeframe*_offline_time**: the amount of time the machine has been offline

### Efficiency KPIs

These are the KPIs that control the amount of time the machine takes to finish a job, calculating various data to see if it's going at cruise speed

- ***metric*_*timeframe*_online_percentage**: (*avg_on_timeframe*[working_time/24 %]) the _metric_ percentage of time the machine has been online during the _timeframe_
- ***metric*_*timeframe*_used_percentage**: (*avg_on_timeframe*[working_time - idle_time/24 %]) the _metric_ percentage of time the machine has been used during the _timeframe_
- ***metric*_*timeframe*_cycle_time**: the _metric_ time the machine does one of it's cycles.

## Output KPIs

These KPIs define the metrics of which we analyze the output batches. We need to watch both for profit and see if we are respecting law regulations

- ***metric*_*timeframe*_processed_material**: The _metric_ amount of processed material produced in a _timeframe_

### Finance KPIs

These KPIs are here to check if the amount of processed material we produced is valued and how much profit is probably going to make.

- **sell_cost_processed_material_per_unit**: Current amount of value the processed material will be sold per unit
- **buy_cost_raw_material_per_unit**: Current amount of value of the raw material per unit
- ***metric*_*timeframe*_energy_cost_per_machine**: The _metric_ amount of energy cost of a machine during the _timeframe_
- **expected_profit_per_unit**: (sell_cost_processed_material_per_unit - buy_cost_raw_material_per_unit) the amount of expected profit given only the material costs.
- **average_daily_expected_profit**: (*avg_on_day*[average_daily_processed_material * (expected_profit_per_unit)]) The average amount of profit expected from the daily batch

### Quality KPIs

These KPIs check if the processed material we got is up to our standard of quality.

- ***metric*_*timeframe*_impurities_in_processed_material**: The amount of impurities found in the processed material in _metric_ during _timeframe_

### Enviroment KPIs

These KPIs are useful to check if we are going overboard with CO2 wastes or similar.

- ***metric*_*timeframe*_discarded_material**: The amount of discarded waste we made in _metric_ during _timeframe_

## Resource KPIs

These are the KPIs that define all the resources the factory is going to use. This include both the Raw Materials and the Energy used to power up the machines.

### Energy KPIs

These are the KPIs that define the energy used in our factory. Energy is related to the power that aliment the machines, and not the raw materials. 

- ***metric*_*timeframe*_energy_consumption_working**: The _metric_ amount of energy that is consumed in a _timeframe_ while the machine is working
- ***metric*_*timeframe*_energy_consumption_idle**: The _metric_ amount of energy that is consumed in a _timeframe_ while the machine is idle

### Material Consumption KPIs

These are the KPIs that define the raw material consumption of the factory. These are used to check how much 

- ***metric*_*timeframe*_raw_material_consumption_working**: The _metric_ amount of raw materials that is consumed in a _timeframe_ while the machine is working
- ***metric*_*timeframe*_raw_material_consumption_idle**: The _metric_ amount of raw materials that is consumed in a _timeframe_ while the machine is idle

## Health KPIs

These are the KPIs that check the health of everything in the factory. Both employee and machines are checked to see if they are into the limits of good efficiency

- ***metric*_*timeframe*_good_cycles**: The _metric_ of good cycles during _timeframe_
- ***metric*_*timeframe*_bad_cycles**: The _metric_ of bad cycles during _timeframe_
- ***machine*_age**: The amount of years a machine have.
- ***machine*_repairs_until_now**: The amount of time a machine has been repaired until now.

### Safety KPIs

These KPIs serve the purpose of check the machine status and how much are the currently safe.

- ***machine*_risk_of_failure**: The risk of a machine to fail

### Employee KPIs

These KPIs are here to see if there are any problems in the behaviour of the employees, so to intervene in case.

- ***machine*_human_intervention**: the amount of time the machine needed an employee to check on it.