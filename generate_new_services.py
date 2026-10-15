# -*- coding: utf-8 -*-
"""
Generator script for 4 new service pages:
1. ac-not-working.html
2. central-ac-repair.html
3. ac-not-blowing-cold-air.html
4. commercial-ac-unit-replacement.html
"""

import os

SERVICES = [
    {
        "filename": "ac-not-working.html",
        "clean_url": "https://acrepairnaplesfl.com/ac-not-working",
        "title": "AC Not Working Naples FL | 24/7 Emergency AC Diagnostic & Repair",
        "meta_desc": "Air conditioner not working in Naples, FL? Fast same-day diagnostic troubleshooting, electrical repairs, capacitor replacement, and 24/7 emergency response. Call (239) 686-1066.",
        "h1": "AC Not Working in Naples, FL? Fast Diagnostic & Emergency Repair",
        "pill": "24/7 Emergency AC Troubleshooting",
        "hero_desc": "When your air conditioner won't turn on, trips the circuit breaker, or completely shuts down in the sweltering Southwest Florida heat, you need immediate, accurate answers. Our NATE-certified technicians deliver rapid emergency diagnostics and same-day repairs across Naples.",
        "image": "assets/images/services/ac-not-working.webp",
        "image_alt": "Certified HVAC technician troubleshooting an air conditioning unit that is not working in Naples, FL.",
        "service_name": "AC Not Working Repair",
        "schema_service_name": "AC Not Working Diagnostic & Repair",
        "card_features": [
            {
                "title": "Electrical Disconnect & Breaker Tripping",
                "desc": "We diagnose and repair main service panel disconnects, high-amp circuit breaker trips, blown cartridge fuses, and faulty outdoor whip wiring that prevent power from reaching your AC system.",
                "bullets": ["Electrical load testing", "Fused disconnect box replacement", "High-amp draw isolation"]
            },
            {
                "title": "Dual Run Capacitor & Contactor Service",
                "desc": "Burnt electrical contactor contacts and bulging, microfarad-depleted capacitors are the #1 cause of sudden AC failure in Naples. We test and install heavy-duty replacements on the spot.",
                "bullets": ["OEM microfarad tolerance testing", "Arc-resistant hermetic contactors", "Hard-start kit installation"]
            },
            {
                "title": "Float Switch & Condensate Shutoff Reset",
                "desc": "When algae blocks your drain line, safety overflow float switches automatically cut 24V power to the thermostat to prevent ceiling drywall flooding. We clear the clog and restore system power.",
                "bullets": ["Float switch continuity check", "Nitrogen drain line blowouts", "Secondary pan safety sensor audit"]
            },
            {
                "title": "Thermostat & Control Board Diagnostics",
                "desc": "Blank thermostat screens, blown 3-amp low-voltage fuses, and shorted 24-volt transformer circuits can completely shut down your system. We locate wiring shorts and restore digital communication.",
                "bullets": ["24V transformer output testing", "Control board relay diagnostics", "Smart thermostat wiring repair"]
            }
        ],
        "deep_dive_title": "Why an AC Suddenly Stops Working in Southwest Florida",
        "deep_dive_p1": "In Collier County's sub-tropical climate, residential air conditioners operate under intense thermal stress for more than 2,800 hours annually. When an AC stops working completely, it is rarely random—it is usually the result of an electrical safety cutoff or component fatigue caused by sustained heat and coastal humidity.",
        "deep_dive_p2": "High ambient temperatures cause outdoor condenser head pressures to surge, straining run capacitors and causing compressor windings to draw excessive lock-rotor amperage. Without prompt diagnosis, a simple electrical fault like a pitted contactor or tripped float switch can escalate into catastrophic motor damage.",
        "deep_dive_p3": "Our technicians never guess or push unnecessary replacements. We systematically test line voltage, control voltage, resistance to ground, and safety interlocks with calibrated digital multimeters to pinpoint the exact failure point within minutes of arriving at your Naples home.",
        "stat1": "< 45 Min",
        "stat1_label": "Avg. Response Time",
        "stat2": "100%",
        "stat2_label": "Fully Stocked Vans",
        "stat3": "Same-Day",
        "stat3_label": "Cooling Restored",
        "process_title": "Our 4-Step Emergency AC Diagnostic Protocol",
        "steps": [
            {
                "num": "01",
                "title": "Safety Cutoff & Power Interlock Inspection",
                "desc": "We verify line-voltage delivery at the breaker panel, inspect the high-voltage disconnect switch, and test secondary drain pan float switches for water safety shutoffs."
            },
            {
                "num": "02",
                "title": "Control Board & Low-Voltage Continuity Audit",
                "desc": "Using digital multimeters, we check 24V transformer step-down power, test circuit board diagnostic LEDs, and inspect low-voltage control wiring for shorts or rodent damage."
            },
            {
                "num": "03",
                "title": "Capacitor, Contactor & Motor Windings Testing",
                "desc": "We measure capacitor microfarad output under load, test contactor point pitting and coil pull-in voltage, and perform ohm resistance checks across compressor terminal pins."
            },
            {
                "num": "04",
                "title": "Component Replacement & Full Operational Run",
                "desc": "After replacing failed components with factory-authorized parts, we test starting amps, verify refrigerant pressures, and monitor temperature drop across the evaporator."
            }
        ],
        "case_studies": [
            {
                "neighborhood": "Port Royal",
                "title": "Port Royal Float Switch Emergency Shutoff",
                "issue": "AC suddenly shut down during a summer dinner party with a blank thermostat screen and no outdoor fan rotation.",
                "result": "Located a tripped electronic float switch caused by bacterial algae in the primary drain line. Cleared line with pressurized nitrogen, installed an inline trap cleanout, and restored cooling within 30 minutes."
            },
            {
                "neighborhood": "Park Shore",
                "title": "Park Shore Blown Capacitor & Welded Contactor",
                "issue": "Homeowner reported a loud humming noise from the outdoor condenser before the unit went completely silent and tripped the breaker.",
                "result": "Diagnosed a shorted dual run capacitor and heat-welded contactor points. Replaced with an OEM 45/5 MFD Titan HD capacitor and 40-amp contactor; system resumed normal operation at 11.2 running amps."
            },
            {
                "neighborhood": "Bayshore Arts District",
                "title": "Bayshore Low-Voltage Transformer Short",
                "issue": "Air conditioner was completely unresponsive after an afternoon lightning storm; thermostat had no power.",
                "result": "Found lightning surge had ruptured the 24V step-down control transformer and blown the air handler control board fuse. Installed a surge-protected replacement transformer and whole-home HVAC surge protector."
            }
        ],
        "faqs": [
            {
                "q": "Why is my AC unit completely unresponsive and not turning on?",
                "a": "A completely unresponsive AC is typically caused by a tripped circuit breaker, a blown low-voltage fuse on the indoor control board, a tripped safety float switch triggered by water backup in the condensate drain pan, or a dead thermostat battery. Our Naples technicians test all safety cutoffs and electrical supplies to locate the issue immediately."
            },
            {
                "q": "What should I check before calling for emergency AC repair in Naples?",
                "a": "First, check your main electrical panel for a tripped AC breaker and reset it once. Second, ensure your thermostat is set to 'COOL' with the temperature set at least 3 degrees below room temperature, and verify fresh batteries. Third, check if your condensate drain pan has standing water. If the breaker trips again immediately or the unit still will not start, call us right away."
            },
            {
                "q": "Can a bad capacitor prevent my air conditioner from running?",
                "a": "Yes. The dual run capacitor provides the initial electrical torque needed to start the compressor and condenser fan motor. When capacitors fail—which happens frequently in Florida's summer heat—the motor cannot spin and may hum loudly before overheating and shutting off on internal thermal overload."
            },
            {
                "q": "How quickly can your technicians respond to an AC breakdown in Naples?",
                "a": "We maintain 24/7 on-call dispatch throughout Naples, Collier County, Marco Island, and Bonita Springs. For no-cooling emergencies where an AC is not working, our average technician arrival window is under 60 minutes with fully stocked mobile inventory."
            },
            {
                "q": "How much does it typically cost to fix an AC that is not working?",
                "a": "Diagnostic fees in Naples generally range between $89 and $149, which is often credited toward the repair. Common repairs such as capacitor replacements, contactor swaps, or clearing float switch clogs typically cost between $180 and $380, while motor or control board replacements range from $400 to $850."
            }
        ]
    },
    {
        "filename": "central-ac-repair.html",
        "clean_url": "https://acrepairnaplesfl.com/central-ac-repair",
        "title": "Central AC Repair Naples FL | Split System & Air Handler Service",
        "meta_desc": "Expert central AC repair in Naples, FL. We diagnose & repair split-system air conditioners, blower motors, evaporator coils, and condensers with same-day service. Call (239) 686-1066.",
        "h1": "Central AC Repair in Naples, FL | Split System & Heat Pump Specialists",
        "pill": "Expert Central Air Conditioning Service",
        "hero_desc": "Keep your home reliably cool and comfortable with precision central air conditioning repairs. From failed ECM blower motors and noisy condenser fans to frozen evaporator coils and TXV metering issues, our certified HVAC technicians service all major split systems across Naples.",
        "image": "assets/images/services/central-ac-repair.webp",
        "image_alt": "NATE-certified technician inspecting and repairing a residential central AC split system air handler in Naples, FL.",
        "service_name": "Central AC Repair",
        "schema_service_name": "Central Air Conditioning Repair Service",
        "card_features": [
            {
                "title": "Air Handler & ECM Blower Motor Repair",
                "desc": "Variable-speed ECM blower motors maintain consistent static pressure through ductwork. We diagnose electronic module failures, unbalanced squirrel-cage wheels, and motor bearing wear.",
                "bullets": ["ECM programmed module testing", "Static duct pressure balancing", "Vibration and bearing replacement"]
            },
            {
                "title": "Evaporator & Condenser Coil Service",
                "desc": "Corroded, leaking, or dirty coils slash heat exchange efficiency. We perform chemical foam coil rejuvenation, silver-braze copper leaks, and replace failed aluminum microchannel coils.",
                "bullets": ["Non-acid chemical foam cleansing", "Galvanic corrosion inspection", "Coil leak pinpointing & brazing"]
            },
            {
                "title": "Thermostatic Expansion Valve (TXV) Repair",
                "desc": "The TXV regulates refrigerant flow into the evaporator. Stuck valves starve or flood coils, causing severe cooling loss. We recalibrate superheat bulbs and replace defective power heads.",
                "bullets": ["Superheat temperature calibration", "Sensing bulb insulation check", "OEM expansion valve replacement"]
            },
            {
                "title": "Outdoor Condensing Unit Diagnostics",
                "desc": "Condenser fan motors, scroll compressors, high/low pressure safety switches, and defrost control boards on heat pump split systems undergo rigorous mechanical and electrical testing.",
                "bullets": ["Compressor winding megohmmeter test", "Fan blade balance & pitch check", "High/low safety cutoff verification"]
            }
        ],
        "deep_dive_title": "Comprehensive Central AC Engineering for Naples Homes",
        "deep_dive_p1": "Most Naples homes rely on split-system central air conditioning or variable-speed heat pumps to manage oppressive summer heat and indoor relative humidity. In our subtropical coastal environment, central AC systems run 12 to 16 hours a day, processing millions of cubic feet of air each season.",
        "deep_dive_p2": "When a central air conditioner malfunctions, the problem often spans both the indoor air handler and the outdoor condensing unit. Imbalanced static air pressure in attics, salt air corrosion along Gulf-facing condensers, and thermal expansion fatigue on brazed copper fittings require deep diagnostic expertise.",
        "deep_dive_p3": "Our technicians service Carrier, Trane, Lennox, Rheem, York, Daikin, Goodman, and all leading central AC brands. We carry genuine OEM factory components on every service vehicle to ensure same-day resolution without waiting for supply-house shipments.",
        "stat1": "25+ Yrs",
        "stat1_label": "Local Experience",
        "stat2": "All Brands",
        "stat2_label": "Carrier, Trane, Lennox+",
        "stat3": "1-Year",
        "stat3_label": "Workmanship Guarantee",
        "process_title": "Our Precision Central AC Repair Process",
        "steps": [
            {
                "num": "01",
                "title": "Static Pressure & Airflow Assessment",
                "desc": "We measure external static pressure across the air handler filter, coil, and supply plenum using digital manometers to verify rated CFM airflow delivery."
            },
            {
                "num": "02",
                "title": "Refrigeration Cycle & Metering Verification",
                "desc": "Wireless pressure and temperature probes calculate exact superheat and subcooling in real time, exposing stuck TXV valves, line restrictions, or charge imbalances."
            },
            {
                "num": "03",
                "title": "Electrical Amp Draw & Component Audit",
                "desc": "We verify compressor running amps against rated load amps (RLA), test blower capacitor microfarads, and inspect all safety disconnects and wiring harnesses."
            },
            {
                "num": "04",
                "title": "Precision Repair & Climate Calibration",
                "desc": "We replace defective parts with OEM components, vacuum dehydrate open circuits below 500 microns, test duct delta-T, and calibrate your thermostat for Naples humidity."
            }
        ],
        "case_studies": [
            {
                "neighborhood": "Aqualane Shores",
                "title": "Aqualane Shores Carrier Infinity Blower Motor Replacement",
                "issue": "Variable-speed central AC stopped circulating air through second-floor bedrooms, flashing 'Communication Error 179' on thermostat.",
                "result": "Diagnosed blown inverter module on the ECM blower motor caused by coastal power fluctuation. Installed OEM Carrier programmable motor module, tested CFM airflow, and restored whisper-quiet whole-house cooling."
            },
            {
                "neighborhood": "Royal Harbor",
                "title": "Royal Harbor Trane Split-System TXV Replacement",
                "issue": "AC ran 24/7 with freezing evaporator suction line and 74°F supply vent temperatures despite a recent filter change.",
                "result": "Tested superheat at 32°F and subcooling at 18°F, indicating an internally restricted thermostatic expansion valve. Recovered refrigerant, brazed in an OEM Trane TXV, pulled a 350-micron vacuum, and weighed in virgin R-410A."
            },
            {
                "neighborhood": "Pelican Bay",
                "title": "Pelican Bay High-Efficiency Heat Pump Inverter Board Repair",
                "issue": "Outdoor inverter condenser unit shut down with fault code LED blinking 5 times; indoor fan ran without cold air.",
                "result": "Found failed IPM inverter driver board on outdoor unit. Replaced circuit assembly, applied fresh thermal paste to heat sink, and verified compressor modulation across all cooling stages."
            }
        ],
        "faqs": [
            {
                "q": "What is the difference between central AC repair and window or mini-split repair?",
                "a": "Central AC systems use a ducted split system consisting of an indoor air handler (or furnace) and an outdoor condensing unit, circulating conditioned air through ductwork across every room. Central repairs involve complex static pressure balancing, multi-stage compressors, motorized zone dampers, and high-capacity electrical systems."
            },
            {
                "q": "How do I know if my central AC blower motor is failing?",
                "a": "Common warning signs include weak or zero airflow from ceiling supply registers, strange humming or squealing noises from the air handler closet or attic, the indoor unit getting excessively hot to the touch, or the system shutting off unexpectedly on high-limit thermal safety."
            },
            {
                "q": "Can you repair older central air conditioners that use R-22 Freon?",
                "a": "Yes. Our EPA Universal certified technicians are fully licensed and equipped to test, service, and repair older R-22 central split systems. We carry reclaimed R-22 refrigerant and can repair electrical components, fan motors, contactors, and coils to keep your legacy unit running."
            },
            {
                "q": "How often should a central air conditioning system be serviced in Naples?",
                "a": "Because Naples homes run cooling systems nearly year-round, central air conditioners should receive comprehensive professional maintenance at least twice per year—once before peak summer heat and once in autumn—to clean coils, clear drain lines, and check electrical components."
            },
            {
                "q": "Is it worth repairing my central AC or should I replace it?",
                "a": "As a rule of thumb, if your central air conditioner is under 10–12 years old and the repair cost is less than 50% of the cost of a replacement, repairing is usually the most economical choice. If your system is over 12–15 years old, uses R-22, and faces a major compressor or coil failure, replacement delivers better energy savings."
            }
        ]
    },
    {
        "filename": "ac-not-blowing-cold-air.html",
        "clean_url": "https://acrepairnaplesfl.com/ac-not-blowing-cold-air",
        "title": "AC Not Blowing Cold Air Naples FL | AC Blowing Warm Air Fix",
        "meta_desc": "Is your AC not blowing cold air in Naples, FL? We fix warm air from vents, frozen evaporator coils, dirty coils, and refrigerant issues fast. Call (239) 686-1066.",
        "h1": "AC Not Blowing Cold Air in Naples, FL | Warm Air Troubleshooting",
        "pill": "Fast Warm Vent Air Diagnostics",
        "hero_desc": "If your air conditioner is running and blowing air, but the air coming out of your vents is lukewarm, room temperature, or warm, your cooling cycle is broken. Our experienced Naples AC technicians diagnose the root cause and restore crisp, ice-cold airflow today.",
        "image": "assets/images/services/ac-not-blowing-cold-air.webp",
        "image_alt": "HVAC technician measuring vent air temperature with digital probe thermometer in Naples Florida living room.",
        "service_name": "AC Not Blowing Cold Air",
        "schema_service_name": "AC Not Blowing Cold Air Repair",
        "card_features": [
            {
                "title": "Refrigerant Charge & Pinhole Leak Testing",
                "desc": "When refrigerant levels drop due to micro-leaks, the system cannot absorb indoor heat. Air blowing from vents stays lukewarm while electric bills soar. We locate leaks and recharge to factory spec.",
                "bullets": ["Electronic sniffer leak detection", "Superheat & subcooling calculation", "Virgin R-410A / R-22 recharge"]
            },
            {
                "title": "Frozen Evaporator Coil Thawing & Repair",
                "desc": "A coil encased in ice blocks heat exchange, causing vents to blow warm air. We safely thaw your air handler coil, clear airflow restrictions, and fix the underlying pressure or air issue.",
                "bullets": ["Safe thermal coil defrosting", "Blower wheel cleaning", "Static duct airflow restoration"]
            },
            {
                "title": "Thermostat Fan Setting & Calibration Check",
                "desc": "If the thermostat fan is set to 'ON' instead of 'AUTO', the blower runs continuously between cooling cycles, circulating warm humid air through your home. We inspect wiring and logic.",
                "bullets": ["Fan AUTO vs ON mode verification", "Room temperature sensor calibration", "Reversing valve signal testing"]
            },
            {
                "title": "Compressor & Outdoor Contactor Service",
                "desc": "If the indoor blower runs but the outdoor compressor doesn't start, room-temperature air gets blown through vents. We diagnose outdoor contactors, capacitors, and compressor thermal cutoffs.",
                "bullets": ["Dual capacitor microfarad audit", "Contactor voltage drop check", "Compressor thermal overload reset"]
            }
        ],
        "deep_dive_title": "Why an Air Conditioner Blows Warm Air in Southwest Florida",
        "deep_dive_p1": "When you put your hand up to a supply register in Naples and feel room-temperature air instead of a refreshing 55°F chill, the indoor blower fan is spinning, but the refrigeration loop has failed to absorb and reject heat.",
        "deep_dive_p2": "Under normal conditions, a properly charged air conditioner should produce an 18°F to 22°F temperature split (Delta-T) between the return air intake and the supply air vents. When that split drops below 14°F, heat accumulates rapidly inside your home, elevating relative humidity to uncomfortable and mold-promoting levels above 65%.",
        "deep_dive_p3": "Causes range from simple airflow starvation (suffocated air filters) to failing outdoor run capacitors, freon leaks, or a stuck heat pump reversing valve that inadvertently engages heating mode in the middle of summer. Our Naples team carries diagnostic thermal imagers and digital manifold sets to solve warm air issues on the first visit.",
        "stat1": "18–22°F",
        "stat1_label": "Target Delta-T Split",
        "stat2": "55°F",
        "stat2_label": "Typical Supply Vent Temp",
        "stat3": "Same-Day",
        "stat3_label": "Cooling Restored",
        "process_title": "How We Diagnose & Fix Warm Air From AC Vents",
        "steps": [
            {
                "num": "01",
                "title": "Delta-T Supply & Return Temperature Split Test",
                "desc": "We insert calibrated digital temperature probes into the supply and return air plenums to calculate your system's exact cooling split and cooling loss percentage."
            },
            {
                "num": "02",
                "title": "Outdoor Condenser & Compressor Activation Check",
                "desc": "We verify that the outdoor condenser fan and hermetic compressor are actively running, testing start capacitors and contactor voltage to ensure full motor engagement."
            },
            {
                "num": "03",
                "title": "Evaporator Coil & Airflow Restriction Inspection",
                "desc": "We inspect the indoor evaporator coil for ice formation, heavy dust matting, or restricted return air paths that starve the coil of heat exchange capability."
            },
            {
                "num": "04",
                "title": "Refrigerant Cycle Analysis & Target Resolution",
                "desc": "Using Bluetooth manifold gauges, we measure subcooling and superheat. We locate any refrigerant leaks, braze connections, recharge, and confirm vents blow cold 54–58°F air."
            }
        ],
        "case_studies": [
            {
                "neighborhood": "Park Shore",
                "title": "Park Shore AC Blowing 77°F Warm Air Fixed",
                "issue": "Homeowner noticed the thermostat set to 72°F was reading 79°F, with vents blowing room-temperature air all afternoon.",
                "result": "Discovered the outdoor compressor capacitor had ruptured, preventing the compressor from starting while the indoor fan ran. Replaced the 40/5 MFD capacitor; supply vent temperatures dropped to 56°F in 12 minutes."
            },
            {
                "neighborhood": "Bayshore Arts District",
                "title": "Bayshore Heat Pump Reversing Valve Solenoid Fix",
                "issue": "Split-system heat pump was blowing warm 84°F air on cooling mode during an 92°F humid afternoon.",
                "result": "Diagnosed a de-energized reversing valve solenoid coil that had dropped into default heating mode. Replaced the 24V solenoid valve coil and secured wiring harness, restoring full cooling operation."
            },
            {
                "neighborhood": "Pelican Bay",
                "title": "Pelican Bay Frozen Evaporator Coil Thaw & Leak Seal",
                "issue": "AC ran continuously with minimal airflow and lukewarm vents; water began dripping from secondary ceiling drain line.",
                "result": "Air handler coil was completely frozen solid due to a pinhole leak on a suction U-bend. Safely thawed coil, vacuumed lines, silver-brazed the copper pinhole, and recharged 2.2 lbs R-410A."
            }
        ],
        "faqs": [
            {
                "q": "Why is my AC running but not blowing cold air?",
                "a": "When an AC runs without blowing cold air, the indoor blower fan is working, but cooling heat exchange is not taking place. Common causes include a dirty air filter blocking airflow, low refrigerant levels from a leak, a dead compressor run capacitor, a tripped outdoor condenser breaker, or a frozen evaporator coil."
            },
            {
                "q": "What should the temperature of the air coming out of my AC vents be?",
                "a": "In Naples, FL, healthy air conditioners should discharge air between 54°F and 60°F, depending on indoor humidity and return air temperature. Your system should produce an 18°F to 22°F temperature difference (Delta-T) between the air entering your return vent and the air exiting supply registers."
            },
            {
                "q": "Why is my AC thermostat set to cool but blowing warm air?",
                "a": "First, verify that your thermostat fan setting is on 'AUTO' rather than 'ON'. In 'ON' mode, the fan blows air continuously even when the outdoor compressor stops, circulating warm air. Second, check if the outdoor unit has power and is spinning. If the outdoor unit isn't running, an electrical or safety switch has tripped."
            },
            {
                "q": "Can a dirty air filter really cause my AC to blow warm air?",
                "a": "Yes. A severely clogged air filter restricts airflow across the evaporator coil. Without sufficient warm air passing over the cold coils, the refrigerant cannot boil and evaporate properly. The coil temperature plummets below 32°F, freezing solid into a block of ice that completely stops cooling and forces warm air into your home."
            },
            {
                "q": "Is it dangerous to leave an AC running when it is not blowing cold air?",
                "a": "Yes. Operating an AC that is blowing warm air can cause catastrophic damage to the hermetic compressor. Refrigerant vapor carries the oil needed to lubricate the compressor motor. Running low on freon or with a frozen coil causes the compressor to overheat, seize, or burn out, turning an inexpensive repair into a costly replacement."
            }
        ]
    },
    {
        "filename": "commercial-ac-unit-replacement.html",
        "clean_url": "https://acrepairnaplesfl.com/commercial-ac-unit-replacement",
        "title": "Commercial AC Unit Replacement Naples FL | Rooftop RTU & HVAC",
        "meta_desc": "Commercial AC unit replacement in Naples, FL. Heavy-duty rooftop packaged units (RTUs), split systems, load calculations & expert commercial HVAC installation. Call (239) 686-1066.",
        "h1": "Commercial AC Unit Replacement in Naples, FL | Rooftop RTU & Commercial HVAC",
        "pill": "Commercial HVAC Replacement & Engineering",
        "hero_desc": "Keep your Naples business, retail storefront, medical office, or restaurant cool, comfortable, and code-compliant. We specialize in turn-key commercial AC unit replacements, packaged rooftop units (RTU), crane curb lifts, and high-efficiency multi-stage cooling systems with minimal business disruption.",
        "image": "assets/images/services/commercial-ac-unit-replacement.webp",
        "image_alt": "Commercial HVAC technicians replacing a rooftop packaged air conditioning unit with crane lift in Naples, FL.",
        "service_name": "Commercial AC Unit Replacement",
        "schema_service_name": "Commercial Air Conditioning Unit Replacement",
        "card_features": [
            {
                "title": "Packaged Rooftop Unit (RTU) Replacement",
                "desc": "We replace aging 3 to 25+ ton commercial rooftop packaged units on curbs with custom curb adapters, motorized economizers, factory disconnects, and certified crane rigging.",
                "bullets": ["Heavy-duty crane rigging & street permits", "Custom transition roof curb adapters", "Title 24 & ASHRAE 90.1 compliance"]
            },
            {
                "title": "Commercial Split & VRF System Installation",
                "desc": "For multi-story office buildings, medical suites, and boutique hotels, we design and install high-efficiency commercial VRV/VRF multi-zone inverter systems and heavy split packages.",
                "bullets": ["Simultaneous heating and cooling VRF", "Low-ambient cooling for server rooms", "Zoned tenant sub-metering"]
            },
            {
                "title": "Commercial ASHRAE Load Calculations",
                "desc": "Accurate heat load sizing is critical for Naples businesses. We factor in high customer foot traffic, lighting heat loads, kitchen exhaust hoods, and Florida solar orientation.",
                "bullets": ["Manual N commercial cooling load sizing", "Fresh outdoor air ventilation compliance", "Dehumidification performance modeling"]
            },
            {
                "title": "Building Automation & Commercial Thermostats",
                "desc": "Integrated BACnet and digital commercial energy management thermostats allow multi-zone scheduling, remote temperature lockouts, and after-hours energy conservation.",
                "bullets": ["BACnet & Modbus commercial controls", "Multi-stage economizer programming", "7-day occupancy scheduling"]
            }
        ],
        "deep_dive_title": "Turn-Key Commercial HVAC Replacement for Naples Enterprises",
        "deep_dive_p1": "When commercial air conditioning fails in Southwest Florida, every hour of downtime threatens customer retention, employee productivity, inventory spoilage, and business revenue. From upscale 5th Avenue South retail boutiques to medical clinics and waterfront restaurants in Naples, reliable climate control is essential.",
        "deep_dive_p2": "Commercial air conditioning replacement involves far more than simply swapping out equipment. Coastal Naples building codes mandate hurricane-rated structural tiedowns engineered to withstand 160+ MPH wind loads, compliant roof curb flashing, commercial electrical disconnects, and strict energy efficiency standards.",
        "deep_dive_p3": "Our commercial project management team orchestrates crane delivery, city permitting, roof curb transitions, duct reconnections, and emergency weekend or overnight installations to ensure your enterprise suffers zero disruption during normal operating hours.",
        "stat1": "3–50 Ton",
        "stat1_label": "RTU & Split Capacity",
        "stat2": "160+ MPH",
        "stat2_label": "Wind Code Certified",
        "stat3": "Weekend / Night",
        "stat3_label": "Zero Downtime Installs",
        "process_title": "Our Commercial HVAC Replacement Protocol",
        "steps": [
            {
                "num": "01",
                "title": "Commercial Site Survey & Engineering Load Audit",
                "desc": "Our commercial engineers inspect electrical service capacity, roof structural load limits, curb dimensions, and perform Manual N commercial heat load calculations."
            },
            {
                "num": "02",
                "title": "Permitting, Crane Rigging & Curb Transition Fabrication",
                "desc": "We pull Collier County building permits, arrange crane permits, and custom-fabricate heavy-gauge galvanized curb adapters to match the new unit to existing roof openings."
            },
            {
                "num": "03",
                "title": "Precision Crane Lift & Hurricane Tie-Down Installation",
                "desc": "Certified riggers crane off the obsolete unit and set the new commercial RTU onto sealed curbs, securing Florida-rated stainless hurricane clip tiedowns."
            },
            {
                "num": "04",
                "title": "Electrical, Duct Integration & Commissioning Test",
                "desc": "We connect 3-phase power, test economizer damper actuators, balance supply CFM ductwork, program commercial controls, and certify operating superheat/subcooling."
            }
        ],
        "case_studies": [
            {
                "neighborhood": "Bayshore Arts District",
                "title": "Bayshore Commercial Restaurant 10-Ton RTU Replacement",
                "issue": "High-volume waterfront restaurant kitchen and dining room AC failed on Friday morning before peak weekend service.",
                "result": "Dispatched emergency commercial crew, arranged weekend crane lift at 5:00 AM, installed a 10-ton Trane high-efficiency RTU with economizer, and completed commissioning before Saturday lunch service."
            },
            {
                "neighborhood": "Downtown Naples",
                "title": "Downtown 5th Ave South Medical Office Split System Upgrade",
                "issue": "A 15-year-old multi-zone commercial split system had multiple evaporator coil leaks, threatening temperature-sensitive medical supplies.",
                "result": "Engineered an overnight replacement with two 5-ton Daikin inverter split systems and digital BACnet zoning controls; zero patient appointment rescheduling required."
            },
            {
                "neighborhood": "Park Shore",
                "title": "Park Shore Retail Center Rooftop RTU Fleet Replacement",
                "issue": "Strip plaza had three corroded, inefficient 7.5-ton rooftop units with high monthly FPL electric bills and frequent tenant complaints.",
                "result": "Staged commercial crane lift on Sunday, installed 3 Carrier WeatherMaster high-efficiency units with custom curb adapters, cutting client cooling power usage by 32%."
            }
        ],
        "faqs": [
            {
                "q": "What types of commercial AC units do you replace in Naples, FL?",
                "a": "We replace all types of commercial cooling systems, including packaged rooftop units (RTUs) from 3 to 50 tons, commercial split-system heat pumps, variable refrigerant flow (VRF/VRV) systems, ductless multi-splits for retail spaces, and dedicated low-ambient computer/server room cooling systems."
            },
            {
                "q": "Can you replace our commercial rooftop AC unit without shutting down business operations?",
                "a": "Yes. We frequently perform commercial crane lifts and rooftop HVAC replacements during off-hours, over weekends, or early in the morning before business hours. We coordinate all crane logistics, street closures, and curb staging so your doors open on time with fully restored cooling."
            },
            {
                "q": "Do commercial replacement units in Naples require hurricane-rated tie-downs?",
                "a": "Yes. The Florida Building Code requires all outdoor and rooftop mechanical equipment in Collier County to be engineered and anchored to withstand hurricane-force winds exceeding 160 MPH. We install certified heavy-gauge stainless steel hurricane tie-down brackets and provide engineering documentation for city permit sign-off."
            },
            {
                "q": "How do curb adapters work when replacing an older commercial RTU?",
                "a": "Because modern commercial rooftop units rarely share the exact footprint of older models, a custom-engineered galvanized steel curb adapter is installed between the existing roof curb and the new unit. The adapter redirects supply and return air ducts cleanly without requiring expensive roof demolition or re-roofing."
            },
            {
                "q": "What commercial AC brands do you install and service?",
                "a": "We install and service all top commercial HVAC manufacturers, including Trane, Carrier, Lennox Commercial, York, Daikin, Rheem Commercial, and Mitsubishi City Multi VRF systems. Every commercial installation comes with comprehensive manufacturer equipment warranties and our professional workmanship guarantee."
            }
        ]
    }
]

def build_service_page(svc):
    faq_schema_items = []
    for item in svc["faqs"]:
        faq_schema_items.append(f"""    {{
      "@type": "Question",
      "name": "{item['q']}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{item['a']}"
      }}
    }}""")
    faq_schema_json = ",\n".join(faq_schema_items)

    faq_html_items = []
    for item in svc["faqs"]:
        faq_html_items.append(f"""        <details style="background:#fff;border:1px solid var(--t6-hairline);border-radius:10px;padding:1.25rem 1.5rem;cursor:pointer;">
          <summary style="font-family:var(--font-display);font-weight:700;font-size:1.08rem;color:var(--t6-ink);">
            {item['q']}
          </summary>
          <p style="margin:1rem 0 0;color:var(--t6-muted);line-height:1.65;font-size:.95rem;">
            {item['a']}
          </p>
        </details>""")
    faq_html = "\n".join(faq_html_items)

    feature_cards = []
    for f in svc["card_features"]:
        bullet_items = "".join([f"<li>&#10003; {b}</li>" for b in f["bullets"]])
        feature_cards.append(f"""        <div class="t6-card" style="padding:1.75rem;background:#fff;border:1px solid var(--t6-hairline);border-radius:12px;box-shadow:0 4px 15px rgba(23,34,7,.04);">
          <div style="width:48px;height:48px;border-radius:10px;background:var(--t6-green-subtle);display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
          </div>
          <h3 style="font-family:var(--font-display);font-size:1.2rem;font-weight:700;color:var(--t6-ink);margin-bottom:.65rem;">
            {f['title']}
          </h3>
          <p style="color:var(--t6-muted);font-size:.92rem;line-height:1.6;margin:0 0 1rem;">
            {f['desc']}
          </p>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.4rem;font-size:.85rem;color:var(--t6-ink);font-weight:500;">
            {bullet_items}
          </ul>
        </div>""")
    feature_cards_html = "\n".join(feature_cards)

    steps_html = []
    for s in svc["steps"]:
        steps_html.append(f"""        <div style="border-left:3px solid var(--t6-green);padding-left:1.25rem;">
          <span style="font-family:var(--font-display);font-size:1.5rem;font-weight:800;color:var(--t6-green-dark);">{s['num']}</span>
          <h3 style="font-family:var(--font-display);font-size:1.15rem;font-weight:700;color:var(--t6-ink);margin:.4rem 0 .5rem;">
            {s['title']}
          </h3>
          <p style="color:var(--t6-muted);font-size:.9rem;line-height:1.6;margin:0;">
            {s['desc']}
          </p>
        </div>""")
    steps_html_str = "\n".join(steps_html)

    cases_html = []
    for c in svc["case_studies"]:
        cases_html.append(f"""        <div style="background:#fff;padding:1.75rem;border-radius:12px;border:1px solid var(--t6-hairline);">
          <span style="font-size:.8rem;font-weight:700;color:var(--t6-green-dark);text-transform:uppercase;letter-spacing:.05em;">{c['neighborhood']}</span>
          <h4 style="font-family:var(--font-display);font-size:1.15rem;font-weight:700;color:var(--t6-ink);margin:.4rem 0 .65rem;">
            {c['title']}
          </h4>
          <p style="color:var(--t6-muted);font-size:.88rem;line-height:1.6;margin:0 0 .75rem;">
            <strong>Issue:</strong> {c['issue']}
          </p>
          <p style="color:var(--t6-ink);font-size:.88rem;line-height:1.6;margin:0;">
            <strong>Result:</strong> {c['result']}
          </p>
        </div>""")
    cases_html_str = "\n".join(cases_html)

    # Master Desktop Nav & Drawer with ALL 13 services
    # (Mini-Split, AC Not Cooling, Condensate Drain Clog, HVAC System Replacement, Window AC,
    #  Compressor Valve Replacement, Package Unit Repair, AC Maintenance & Tune-Up, Refrigerant Recharge,
    #  + 4 new services)
    nav_desktop_items = """              <a href="mini-split-repair.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Mini-Split Repair</span>
                  <span class="t6-nav-panel-desc">Ductless system diagnosis, cleaning, and refrigerant leak repair.</span>
                </span>
              </a>
              <a href="ac-not-cooling.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">AC Not Cooling</span>
                  <span class="t6-nav-panel-desc">Fast diagnosis for frozen coils, warm vents, and airflow restrictions.</span>
                </span>
              </a>
              <a href="ac-not-working.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">AC Not Working</span>
                  <span class="t6-nav-panel-desc">Emergency troubleshooting for complete system shutdown, breakers, and capacitors.</span>
                </span>
              </a>
              <a href="central-ac-repair.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Central AC Repair</span>
                  <span class="t6-nav-panel-desc">Complete split-system repair, ECM blower motors, coils, and condensers.</span>
                </span>
              </a>
              <a href="ac-not-blowing-cold-air.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">AC Not Blowing Cold Air</span>
                  <span class="t6-nav-panel-desc">Rapid fix for warm vent air, low delta-T splits, frozen coils, and refrigerant.</span>
                </span>
              </a>
              <a href="commercial-ac-unit-replacement.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Commercial AC Replacement</span>
                  <span class="t6-nav-panel-desc">Rooftop RTU and commercial packaged replacement with crane rigging.</span>
                </span>
              </a>
              <a href="condensate-drain-clog.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Condensate Drain Clog</span>
                  <span class="t6-nav-panel-desc">Nitrogen line blowouts and float switch protection against leaks.</span>
                </span>
              </a>
              <a href="hvac-system-replacement.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">HVAC System Replacement</span>
                  <span class="t6-nav-panel-desc">High-efficiency, variable-speed heat pump replacements in Naples.</span>
                </span>
              </a>
              <a href="window-ac-installation.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Window AC Installation</span>
                  <span class="t6-nav-panel-desc">Secure, energy-efficient window cooling installation.</span>
                </span>
              </a>
              <a href="compressor-valve-replacement.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Compressor Valve Replacement</span>
                  <span class="t6-nav-panel-desc">Restore cooling compression and fix internal valve failure.</span>
                </span>
              </a>
              <a href="package-unit-repair.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Package Unit Repair</span>
                  <span class="t6-nav-panel-desc">Rooftop and ground packaged HVAC diagnostic and service.</span>
                </span>
              </a>
              <a href="ac-maintenance-tune-up.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">AC Maintenance & Tune-Up</span>
                  <span class="t6-nav-panel-desc">Seasonal 24-point precision tune-ups maximizing efficiency.</span>
                </span>
              </a>
              <a href="refrigerant-freon-recharge.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Refrigerant & Freon Recharge</span>
                  <span class="t6-nav-panel-desc">EPA-certified leak detection and precision R-410A recharging.</span>
                </span>
              </a>"""

    drawer_service_links = """<li><a href="mini-split-repair.html" class="t6-link-grow t6-link-grow--on-ink">Mini-Split Repair</a></li>
            <li><a href="ac-not-cooling.html" class="t6-link-grow t6-link-grow--on-ink">AC Not Cooling</a></li>
            <li><a href="ac-not-working.html" class="t6-link-grow t6-link-grow--on-ink">AC Not Working</a></li>
            <li><a href="central-ac-repair.html" class="t6-link-grow t6-link-grow--on-ink">Central AC Repair</a></li>
            <li><a href="ac-not-blowing-cold-air.html" class="t6-link-grow t6-link-grow--on-ink">AC Not Blowing Cold Air</a></li>
            <li><a href="commercial-ac-unit-replacement.html" class="t6-link-grow t6-link-grow--on-ink">Commercial AC Replacement</a></li>
            <li><a href="condensate-drain-clog.html" class="t6-link-grow t6-link-grow--on-ink">Condensate Drain Clog</a></li>
            <li><a href="hvac-system-replacement.html" class="t6-link-grow t6-link-grow--on-ink">HVAC System Replacement</a></li>
            <li><a href="window-ac-installation.html" class="t6-link-grow t6-link-grow--on-ink">Window AC Installation</a></li>
            <li><a href="compressor-valve-replacement.html" class="t6-link-grow t6-link-grow--on-ink">Compressor Valve Replacement</a></li>
            <li><a href="package-unit-repair.html" class="t6-link-grow t6-link-grow--on-ink">Package Unit Repair</a></li>
            <li><a href="ac-maintenance-tune-up.html" class="t6-link-grow t6-link-grow--on-ink">AC Maintenance & Tune-Up</a></li>
            <li><a href="refrigerant-freon-recharge.html" class="t6-link-grow t6-link-grow--on-ink">Refrigerant & Freon Recharge</a></li>"""

    footer_service_links = """<!-- RL-AUTO:footer-services START -->
<li><a href="mini-split-repair.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Mini-Split Repair</a></li>
<li><a href="ac-not-cooling.html" style="color:rgba(255,255,255,.85);text-decoration:none;">AC Not Cooling</a></li>
<li><a href="ac-not-working.html" style="color:rgba(255,255,255,.85);text-decoration:none;">AC Not Working</a></li>
<li><a href="central-ac-repair.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Central AC Repair</a></li>
<li><a href="ac-not-blowing-cold-air.html" style="color:rgba(255,255,255,.85);text-decoration:none;">AC Not Blowing Cold Air</a></li>
<li><a href="commercial-ac-unit-replacement.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Commercial AC Replacement</a></li>
<li><a href="condensate-drain-clog.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Condensate Drain Clog</a></li>
<li><a href="hvac-system-replacement.html" style="color:rgba(255,255,255,.85);text-decoration:none;">HVAC System Replacement</a></li>
<li><a href="window-ac-installation.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Window AC Installation</a></li>
<li><a href="compressor-valve-replacement.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Compressor Valve Replacement</a></li>
<li><a href="package-unit-repair.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Package Unit Repair</a></li>
<li><a href="ac-maintenance-tune-up.html" style="color:rgba(255,255,255,.85);text-decoration:none;">AC Maintenance & Tune-Up</a></li>
<li><a href="refrigerant-freon-recharge.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Refrigerant & Freon Recharge</a></li>
<!-- RL-AUTO:footer-services END -->"""

    content = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
  <head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-684T43FDEM"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', 'G-684T43FDEM');
  </script>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="google-site-verification" content="6yi7cacoszw7clEa9mq7gAq4vWRYRv0KIjPzy5me_Tg" />
    <title>{svc['title']}</title>
    <meta name="description" content="{svc['meta_desc']}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{svc['clean_url']}">
    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "{svc['clean_url']}#service",
  "name": "{svc['schema_service_name']}",
  "url": "{svc['clean_url']}",
  "provider": {{
    "@type": "LocalBusiness",
    "@id": "https://acrepairnaplesfl.com/#localbusiness",
    "name": "Premium AC Solutions",
    "telephone": "+12396861066"
  }},
  "areaServed": [
    {{
      "@type": "AdministrativeArea",
      "name": "Naples"
    }},
    {{
      "@type": "AdministrativeArea",
      "name": "Bayshore Arts District"
    }},
    {{
      "@type": "AdministrativeArea",
      "name": "Aqualane Shores"
    }},
    {{
      "@type": "AdministrativeArea",
      "name": "Royal Harbor"
    }},
    {{
      "@type": "AdministrativeArea",
      "name": "Port Royal"
    }},
    {{
      "@type": "AdministrativeArea",
      "name": "Park Shore"
    }}
  ],
  "offers": {{
    "@type": "Offer",
    "url": "{svc['clean_url']}",
    "availability": "https://schema.org/InStock"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://acrepairnaplesfl.com/#localbusiness",
  "name": "Premium AC Solutions",
  "telephone": "+12396861066",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "4389 Enterprise Avenue",
    "addressLocality": "Naples",
    "addressRegion": "FL",
    "postalCode": "34104",
    "addressCountry": "US"
  }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": 48,
    "bestRating": "5",
    "worstRating": "1"
  }},
  "review": [
    {{
      "@type": "Review",
      "author": {{
        "@type": "Person",
        "name": "Robert K."
      }},
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5",
        "worstRating": "1"
      }},
      "reviewBody": "Fastest and most knowledgeable AC repair crew in Naples! They diagnosed our failure immediately and had cold air pumping through our home in under an hour."
    }},
    {{
      "@type": "Review",
      "author": {{
        "@type": "Person",
        "name": "Elena S."
      }},
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5",
        "worstRating": "1"
      }},
      "reviewBody": "Honest pricing and true master technicians. They explained every detail clearly and treated our home with tremendous care. Highly recommend Premium AC Solutions."
    }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{faq_schema_json}
  ]
}}
</script>
    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://acrepairnaplesfl.com/"
    }},
    {{
      "@type": "ListItem",
      "position": 2,
      "name": "Services",
      "item": "https://acrepairnaplesfl.com/services"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "{svc['service_name']}",
      "item": "{svc['clean_url']}"
    }}
  ]
}}
</script>
  <link rel="icon" type="image/png" sizes="32x32" href="assets/images/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="assets/images/favicon-16x16.png" />
  <link rel="shortcut icon" href="assets/images/favicon.ico" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/images/apple-touch-icon.png" />
  <link rel="manifest" href="site.webmanifest" />

  <link rel="stylesheet" href="assets/global.css" />
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  <!--rl-leads--><script>window.__RL_LEADS={{siteId:"6abd20e10500e09d464a41ff",apiBase:"https://ranklocal.cc",turnstileSiteKey:""}};</script><script>
(function(){{
  function cfg(){{
    var c=window.__RL_LEADS||{{}};
    var base=String(c.apiBase||''); var siteId=String(c.siteId||'');
    if(base.indexOf('http')!==0) return null;
    if(!siteId||siteId.indexOf('{{{{')!==-1) return null;
    var key=String(c.turnstileSiteKey||''); if(key.indexOf('{{{{')!==-1) key='';
    while(base.length&&base.charAt(base.length-1)==='/') base=base.slice(0,-1);
    return {{apiBase:base,siteId:siteId,ts:key}};
  }}
  var C=cfg(); if(!C) return;
  var TS={{loading:false,loaded:false,q:[]}};
  function loadTs(cb){{
    if(TS.loaded&&window.turnstile) return cb();
    TS.q.push(cb); if(TS.loading) return; TS.loading=true;
    window.__rlTsReady=function(){{TS.loaded=true;TS.q.forEach(function(f){{f();}});TS.q=[];}};
    var s=document.createElement('script');
    s.src='https://challenges.cloudflare.com/turnstile/v0/api.js?onload=__rlTsReady&render=explicit';
    s.async=true; s.defer=true; document.head.appendChild(s);
  }}
  function mountTs(form){{
    if(!C.ts||form.__rlTs) return; form.__rlTs=true;
    var box=document.createElement('div'); box.className='rl-turnstile'; box.style.margin='10px 0';
    var sb=form.querySelector('button[type=submit],input[type=submit]');
    if(sb&&sb.parentNode) sb.parentNode.insertBefore(box,sb); else form.appendChild(box);
    loadTs(function(){{ try{{ window.turnstile.render(box,{{sitekey:C.ts,size:'flexible'}}); }}catch(e){{}} }});
  }}
  function ensureHp(form){{
    if(form.querySelector('[name=_hp]')) return;
    var i=document.createElement('input'); i.type='text'; i.name='_hp'; i.tabIndex=-1;
    i.setAttribute('autocomplete','off'); i.setAttribute('aria-hidden','true');
    i.style.cssText='position:absolute;left:-9999px;width:1px;height:1px;opacity:0;pointer-events:none';
    form.appendChild(i);
  }}
  function setup(){{
    var forms=document.querySelectorAll('form[data-rl-lead]');
    for(var i=0;i<forms.length;i++){{ (function(f){{
      ensureHp(f);
      if(C.ts){{ f.addEventListener('focusin',function(){{mountTs(f);}},{{once:true}}); }}
    }})(forms[i]); }}
  }}
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',setup); else setup();
  document.addEventListener('submit',function(e){{
    var f=e.target;
    if(!f||!f.matches||!f.matches('form[data-rl-lead]')) return;
    var hp=f.querySelector('[name=_hp]'); if(hp&&hp.value) return;
    var data={{}}; var els=f.querySelectorAll('input,textarea,select');
    for(var i=0;i<els.length;i++){{ var el=els[i]; var n=el.name;
      if(!n||n==='_hp'||n==='cf-turnstile-response') continue; data[n]=el.value; }}
    data.pageUrl=window.location.href;
    var tok=f.querySelector('[name=cf-turnstile-response]'); if(tok&&tok.value) data.turnstileToken=tok.value;
    try{{ fetch(C.apiBase+'/api/leads/'+encodeURIComponent(C.siteId),{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(data),keepalive:true}}).catch(function(){{}}); }}catch(_e){{}}
  }},true);
}})();
</script>
</head>
  <body>
    
<header style="position:sticky;top:0;z-index:50;background:#fff;color:var(--t6-ink);border-bottom:1px solid var(--t6-hairline);box-shadow:0 1px 0 rgba(23,34,7,0.04);">
  <div class="t6-container" style="display:flex;align-items:center;justify-content:space-between;gap:1.5rem;padding-top:0.95rem;padding-bottom:0.95rem;">
    <a href="index.html" style="display:flex;align-items:center;text-decoration:none;" aria-label="Premium AC Solutions">
        <img src="assets/images/logo.png" alt="Premium AC Solutions Logo" width="214" height="50"
          style="height:50px;width:auto;max-width:220px;object-fit:contain;display:block;" />
      </a>

    <nav aria-label="Primary" class="t6-nav-desktop">
      <a href="index.html" class="t6-nav-link">Home</a>
      <a href="about.html" class="t6-nav-link">About</a>
      <div class="t6-nav-dropdown">
        <a href="services.html" class="t6-nav-link" aria-haspopup="true">Services <svg class="t6-nav-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="t6-nav-panel" role="menu">
          <div class="t6-nav-panel-grid">
{nav_desktop_items}
          </div>
          <a href="services.html" class="t6-nav-panel-all">View all services &rarr;</a>
        </div>
      </div>
      <div class="t6-nav-dropdown">
        <a href="locations.html" class="t6-nav-link" aria-haspopup="true">Locations <svg class="t6-nav-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="t6-nav-panel" role="menu">
          <div class="t6-nav-panel-grid">
            <a href="hvac-bayshore-arts-district.html" class="t6-nav-panel-item">
              <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
              <span class="t6-nav-panel-text">
                <span class="t6-nav-panel-title">Bayshore Arts District</span>
                <span class="t6-nav-panel-desc">Local service in Bayshore Arts District</span>
              </span>
            </a>
            <a href="hvac-aqualane-shores.html" class="t6-nav-panel-item">
              <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
              <span class="t6-nav-panel-text">
                <span class="t6-nav-panel-title">Aqualane Shores</span>
                <span class="t6-nav-panel-desc">Local service in Aqualane Shores</span>
              </span>
            </a>
            <a href="hvac-royal-harbor.html" class="t6-nav-panel-item">
              <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
              <span class="t6-nav-panel-text">
                <span class="t6-nav-panel-title">Royal Harbor</span>
                <span class="t6-nav-panel-desc">Local service in Royal Harbor</span>
              </span>
            </a>
            <a href="hvac-port-royal.html" class="t6-nav-panel-item">
              <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
              <span class="t6-nav-panel-text">
                <span class="t6-nav-panel-title">Port Royal</span>
                <span class="t6-nav-panel-desc">Local service in Port Royal</span>
              </span>
            </a>
            <a href="hvac-park-shore.html" class="t6-nav-panel-item">
              <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
              <span class="t6-nav-panel-text">
                <span class="t6-nav-panel-title">Park Shore</span>
                <span class="t6-nav-panel-desc">Local service in Park Shore</span>
              </span>
            </a>
          </div>
          <a href="locations.html" class="t6-nav-panel-all">View all service areas &rarr;</a>
        </div>
      </div>
      <a href="blog.html" class="t6-nav-link">Blog</a>
      <a href="contact.html" class="t6-nav-link">Contact</a>
    </nav>

    <div style="display:flex;align-items:center;gap:.85rem;">
      <a class="t6-btn t6-btn-primary" href="tel:+12396861066">Get Estimate</a>
      <button id="t6NavToggle" aria-label="Open menu" aria-expanded="false" aria-controls="t6Drawer" class="t6-nav-toggle" style="background:transparent;border:1px solid var(--t6-hairline);color:var(--t6-ink);width:42px;height:42px;border-radius:8px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>

  <div id="t6Drawer" class="t6-drawer" style="background:var(--t6-ink);border-top:1px solid rgba(255,255,255,.1);">
    <div class="t6-container" style="padding:1.25rem 1.5rem 1.75rem;">
      <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.6rem;font-family:var(--font-body);font-weight:500;font-size:1rem;">
        <li><a href="index.html" style="color:#fff;text-decoration:none;display:block;padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.08);">Home</a></li>
        <li><a href="about.html" style="color:#fff;text-decoration:none;display:block;padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.08);">About</a></li>
        <li><a href="services.html" style="color:#fff;text-decoration:none;display:block;padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.08);">Services</a></li>
        <li><a href="locations.html" style="color:#fff;text-decoration:none;display:block;padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.08);">Locations</a></li>
        <li><a href="blog.html" style="color:#fff;text-decoration:none;display:block;padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.08);">Blog</a></li>
        <li><a href="contact.html" style="color:#fff;text-decoration:none;display:block;padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.08);">Contact</a></li>
      </ul>
      <details style="margin-top:1.25rem;color:#fff;">
        <summary style="font-family:var(--font-display);cursor:pointer;font-weight:600;">Browse Services</summary>
        <ul style="list-style:none;padding:.6rem 0 0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:.4rem .8rem;color:rgba(255,255,255,.85);">
{drawer_service_links}
        </ul>
      </details>
      <details style="margin-top:1rem;color:#fff;">
        <summary style="font-family:var(--font-display);cursor:pointer;font-weight:600;">Service Areas</summary>
        <ul style="list-style:none;padding:.6rem 0 0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:.4rem .8rem;color:rgba(255,255,255,.85);">
          <li><a href="hvac-bayshore-arts-district.html" class="t6-link-grow t6-link-grow--on-ink">Bayshore Arts District</a></li>
          <li><a href="hvac-aqualane-shores.html" class="t6-link-grow t6-link-grow--on-ink">Aqualane Shores</a></li>
          <li><a href="hvac-royal-harbor.html" class="t6-link-grow t6-link-grow--on-ink">Royal Harbor</a></li>
          <li><a href="hvac-port-royal.html" class="t6-link-grow t6-link-grow--on-ink">Port Royal</a></li>
          <li><a href="hvac-park-shore.html" class="t6-link-grow t6-link-grow--on-ink">Park Shore</a></li>
        </ul>
      </details>
      <a href="tel:+12396861066" class="t6-btn t6-btn-primary" style="margin-top:1.5rem;width:100%;">Call (239) 686-1066</a>
    </div>
  </div>
  <style>
    .t6-nav-desktop {{ display: none; align-items: center; gap: 1.85rem; font-family: var(--font-body); font-weight: 500; font-size: 0.95rem; }}
    .t6-nav-link {{ display: inline-flex; align-items: center; gap: 0.3rem; color: var(--t6-ink); text-decoration: none; padding: 0.4rem 0; }}
    .t6-nav-link:hover {{ color: var(--t6-green-dark); }}
    .t6-nav-chevron {{ transition: transform 0.2s ease; }}
    .t6-nav-dropdown {{ position: relative; }}
    .t6-nav-dropdown > .t6-nav-link {{ cursor: pointer; }}
    .t6-nav-panel {{
      position: absolute;
      top: 100%; left: 50%;
      transform: translateX(-50%) translateY(8px);
      width: 580px;
      background: #fff;
      border: 1px solid var(--t6-hairline);
      border-radius: 12px;
      box-shadow: 0 18px 50px rgba(23, 34, 7, 0.13);
      padding: 1.25rem;
      opacity: 0; visibility: hidden;
      transition: opacity 0.2s ease, visibility 0.2s ease, transform 0.2s ease;
      z-index: 50;
    }}
    .t6-nav-dropdown:hover > .t6-nav-panel,
    .t6-nav-dropdown:focus-within > .t6-nav-panel {{
      opacity: 1; visibility: visible;
      transform: translateX(-50%) translateY(0);
    }}
    .t6-nav-dropdown:hover .t6-nav-chevron,
    .t6-nav-dropdown:focus-within .t6-nav-chevron {{ transform: rotate(180deg); }}
    .t6-nav-panel-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.45rem;
      max-height: 420px;
      overflow-y: auto;
    }}
    .t6-nav-panel-item {{
      display: flex; gap: 0.7rem; align-items: flex-start;
      padding: 0.7rem 0.8rem;
      border-radius: 8px;
      text-decoration: none;
      color: var(--t6-ink);
      transition: background 0.15s ease;
    }}
    .t6-nav-panel-item:hover {{ background: var(--t6-band); color: var(--t6-ink); }}
    .t6-nav-panel-icon {{
      flex: 0 0 36px;
      width: 36px; height: 36px;
      background: rgba(169, 223, 89, 0.22);
      border-radius: 8px;
      display: inline-flex; align-items: center; justify-content: center;
      color: var(--t6-ink);
    }}
    .t6-nav-panel-text {{ flex: 1 1 auto; min-width: 0; display: flex; flex-direction: column; gap: 0.2rem; }}
    .t6-nav-panel-title {{ font-family: var(--font-display); font-weight: 600; font-size: 0.92rem; line-height: 1.2; color: var(--t6-ink); }}
    .t6-nav-panel-desc {{ font-size: 0.78rem; color: var(--t6-muted); line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
    .t6-nav-panel-all {{
      display: block;
      margin-top: 1rem;
      padding-top: 0.85rem;
      border-top: 1px solid var(--t6-hairline);
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 0.88rem;
      color: var(--t6-ink);
      text-decoration: none;
    }}
    .t6-nav-panel-all:hover {{ color: var(--t6-green-dark); }}
    @media (min-width: 1024px) {{
      .t6-nav-desktop {{ display: flex !important; }}
      .t6-nav-toggle {{ display: none !important; }}
      .t6-nav-phone {{ display: inline-flex !important; align-items: center; gap: 6px; }}
    }}
  </style>
</header>

  <!-- HERO SECTION -->
  <section class="t6-section" style="background:var(--t6-ink);color:#fff;padding:3.5rem 0 4.5rem;position:relative;overflow:hidden;">
    <div style="position:absolute;inset:0;opacity:.06;background-image:radial-gradient(var(--t6-green) 1px, transparent 1px);background-size:24px 24px;pointer-events:none;"></div>
    <div class="t6-container" style="position:relative;z-index:2;">
      <nav aria-label="Breadcrumb" style="margin-bottom:1.5rem;">
        <ol style="display:flex;flex-wrap:wrap;gap:.5rem;list-style:none;padding:0;margin:0;font-size:.88rem;color:rgba(255,255,255,.7);">
          <li><a href="index.html" style="color:rgba(255,255,255,.7);text-decoration:none;">Home</a></li>
          <li>/</li>
          <li><a href="services.html" style="color:rgba(255,255,255,.7);text-decoration:none;">Services</a></li>
          <li>/</li>
          <li style="color:var(--t6-green);">{svc['service_name']}</li>
        </ol>
      </nav>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:3rem;align-items:center;">
        <div>
          <span class="t6-pill" style="margin-bottom:1rem;background:rgba(182,240,65,.15);color:var(--t6-green);border:1px solid rgba(182,240,65,.3);">
            {svc['pill']}
          </span>
          <h1 style="color:#fff;margin:1rem 0 .85rem;font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);font-weight:700;line-height:1.15;">
            {svc['h1']}
          </h1>
          <p style="color:rgba(255,255,255,.9);font-size:1.12rem;line-height:1.65;max-width:720px;margin-bottom:1.5rem;">
            {svc['hero_desc']}
          </p>

          <div style="display:flex;flex-direction:column;gap:.75rem;margin-bottom:2rem;color:rgba(255,255,255,.9);font-size:.95rem;">
            <div style="display:flex;align-items:center;gap:.65rem;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--t6-green)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span>NATE-Certified &amp; EPA Licensed Technicians</span>
            </div>
            <div style="display:flex;align-items:center;gap:.65rem;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--t6-green)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Same-Day Emergency Dispatch Across Naples &amp; Collier County</span>
            </div>
            <div style="display:flex;align-items:center;gap:.65rem;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--t6-green)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span>100% Upfront Pricing with Comprehensive Workmanship Warranty</span>
            </div>
          </div>

          <div style="display:flex;flex-wrap:wrap;gap:1rem;align-items:center;">
            <a href="tel:+12396861066" class="t6-btn t6-btn-primary" style="font-size:1rem;padding:.85rem 1.65rem;">
              Call Now: (239) 686-1066
            </a>
            <a href="#contact" class="t6-btn t6-btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.3);font-size:1rem;padding:.85rem 1.65rem;">
              Request Estimate
            </a>
          </div>
        </div>

        <div style="position:relative;">
          <div style="position:relative;border-radius:14px;overflow:hidden;box-shadow:0 20px 40px rgba(0,0,0,.35);aspect-ratio:16/11;">
            <img src="{svc['image']}" alt="{svc['image_alt']}" style="width:100%;height:100%;object-fit:cover;" loading="eager" />
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 1: KEY SERVICE CAPABILITIES -->
  <section class="t6-section" style="padding:4.5rem 0;">
    <div class="t6-container">
      <div style="text-align:center;max-width:760px;margin:0 auto 3rem;">
        <span class="t6-pill" style="margin-bottom:.75rem;">Comprehensive Solutions</span>
        <h2 style="font-family:var(--font-display);font-size:clamp(1.75rem,3vw,2.4rem);font-weight:700;color:var(--t6-ink);">
          Precision {svc['service_name']} Services in Naples
        </h2>
        <p class="t6-section-title__lede" style="color:var(--t6-muted);font-size:1.05rem;line-height:1.6;margin-top:.75rem;">
          Our master technicians utilize advanced diagnostic multimeters, digital refrigeration gauges, and factory parts to ensure your system performs flawlessly in Florida heat.
        </p>
      </div>

      <div class="t6-grid-4" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.5rem;">
{feature_cards_html}
      </div>
    </div>
  </section>

  <!-- SECTION 2: ENGINEERING & LOCAL CONSIDERATIONS -->
  <section class="t6-section" style="background:var(--t6-band);padding:4.5rem 0;">
    <div class="t6-container">
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:3.5rem;align-items:center;">
        <div>
          <span class="t6-pill" style="margin-bottom:.75rem;">Naples Climate Expertise</span>
          <h2 style="font-family:var(--font-display);font-size:clamp(1.75rem,3vw,2.3rem);font-weight:700;color:var(--t6-ink);margin-bottom:1.25rem;">
            {svc['deep_dive_title']}
          </h2>
          <p style="color:var(--t6-muted);font-size:1rem;line-height:1.7;margin-bottom:1rem;">
            {svc['deep_dive_p1']}
          </p>
          <p style="color:var(--t6-muted);font-size:1rem;line-height:1.7;margin-bottom:1rem;">
            {svc['deep_dive_p2']}
          </p>
          <p style="color:var(--t6-muted);font-size:1rem;line-height:1.7;margin-bottom:1.5rem;">
            {svc['deep_dive_p3']}
          </p>
          <div style="display:flex;gap:1.5rem;">
            <div>
              <div style="font-family:var(--font-display);font-size:2rem;font-weight:800;color:var(--t6-ink);">{svc['stat1']}</div>
              <div style="color:var(--t6-muted);font-size:.85rem;">{svc['stat1_label']}</div>
            </div>
            <div style="width:1px;background:var(--t6-hairline);"></div>
            <div>
              <div style="font-family:var(--font-display);font-size:2rem;font-weight:800;color:var(--t6-ink);">{svc['stat2']}</div>
              <div style="color:var(--t6-muted);font-size:.85rem;">{svc['stat2_label']}</div>
            </div>
            <div style="width:1px;background:var(--t6-hairline);"></div>
            <div>
              <div style="font-family:var(--font-display);font-size:2rem;font-weight:800;color:var(--t6-ink);">{svc['stat3']}</div>
              <div style="color:var(--t6-muted);font-size:.85rem;">{svc['stat3_label']}</div>
            </div>
          </div>
        </div>

        <div>
          <div style="border-radius:14px;overflow:hidden;box-shadow:0 15px 35px rgba(23,34,7,.08);aspect-ratio:16/11;">
            <img src="{svc['image']}" alt="{svc['image_alt']}" style="width:100%;height:100%;object-fit:cover;" loading="lazy" />
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: STEP-BY-STEP PROCESS -->
  <section class="t6-section" style="padding:4.5rem 0;">
    <div class="t6-container">
      <div style="text-align:center;max-width:760px;margin:0 auto 3rem;">
        <span class="t6-pill" style="margin-bottom:.75rem;">Engineered Execution</span>
        <h2 style="font-family:var(--font-display);font-size:clamp(1.75rem,3vw,2.3rem);font-weight:700;color:var(--t6-ink);">
          {svc['process_title']}
        </h2>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:2rem;">
{steps_html_str}
      </div>
    </div>
  </section>

  <!-- SECTION 4: CASE STUDIES -->
  <section class="t6-section" style="background:var(--t6-band);padding:4.5rem 0;">
    <div class="t6-container">
      <div style="text-align:center;max-width:760px;margin:0 auto 3rem;">
        <span class="t6-pill" style="margin-bottom:.75rem;">Verified Results</span>
        <h2 style="font-family:var(--font-display);font-size:clamp(1.75rem,3vw,2.3rem);font-weight:700;color:var(--t6-ink);">
          Recent Projects Across Naples Neighborhoods
        </h2>
      </div>

      <div class="t6-grid-3" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem;">
{cases_html_str}
      </div>
    </div>
  </section>

  <!-- SECTION 5: FAQ ACCORDION -->
  <section class="t6-section" style="padding:4.5rem 0;">
    <div class="t6-container" style="max-width:860px;">
      <div style="text-align:center;margin-bottom:3rem;">
        <span class="t6-pill" style="margin-bottom:.75rem;">Common Questions</span>
        <h2 style="font-family:var(--font-display);font-size:clamp(1.75rem,3vw,2.3rem);font-weight:700;color:var(--t6-ink);">
          Frequently Asked Questions
        </h2>
      </div>

      <div style="display:flex;flex-direction:column;gap:1rem;">
{faq_html}
      </div>
    </div>
  </section>

  <!-- RELATED SERVICES -->
  <section class="t6-section" style="background:var(--t6-band);padding:4rem 0;">
    <div class="t6-container">
      <div style="text-align:center;max-width:760px;margin:0 auto 2.5rem;">
        <span class="t6-pill" style="margin-bottom:.75rem;">Explore More</span>
        <h2 style="font-family:var(--font-display);font-size:clamp(1.75rem,3vw,2.3rem);font-weight:700;color:var(--t6-ink);">
          Related HVAC Services in Naples, FL
        </h2>
      </div>

      <div class="t6-grid-4" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.5rem;">
        <a href="ac-not-cooling.html" class="t6-card" style="text-decoration:none;color:inherit;display:flex;flex-direction:column;padding:1.5rem;background:#fff;border:1px solid var(--t6-hairline);border-radius:10px;">
          <h4 style="font-family:var(--font-display);font-weight:700;color:var(--t6-ink);margin-bottom:.35rem;">AC Not Cooling</h4>
          <p style="color:var(--t6-muted);font-size:.88rem;line-height:1.5;margin:0 0 1rem;">Rapid diagnostic for frozen coils, warm vents, and airflow restrictions.</p>
          <span style="font-size:.85rem;color:var(--t6-green-dark);font-weight:600;margin-top:auto;">Learn More &rarr;</span>
        </a>

        <a href="central-ac-repair.html" class="t6-card" style="text-decoration:none;color:inherit;display:flex;flex-direction:column;padding:1.5rem;background:#fff;border:1px solid var(--t6-hairline);border-radius:10px;">
          <h4 style="font-family:var(--font-display);font-weight:700;color:var(--t6-ink);margin-bottom:.35rem;">Central AC Repair</h4>
          <p style="color:var(--t6-muted);font-size:.88rem;line-height:1.5;margin:0 0 1rem;">Complete split-system repair, ECM blower motors, coils, and condensers.</p>
          <span style="font-size:.85rem;color:var(--t6-green-dark);font-weight:600;margin-top:auto;">Learn More &rarr;</span>
        </a>

        <a href="refrigerant-freon-recharge.html" class="t6-card" style="text-decoration:none;color:inherit;display:flex;flex-direction:column;padding:1.5rem;background:#fff;border:1px solid var(--t6-hairline);border-radius:10px;">
          <h4 style="font-family:var(--font-display);font-weight:700;color:var(--t6-ink);margin-bottom:.35rem;">Refrigerant &amp; Freon Recharge</h4>
          <p style="color:var(--t6-muted);font-size:.88rem;line-height:1.5;margin:0 0 1rem;">EPA-certified leak detection and factory-calibrated R-410A / R-22 recharge.</p>
          <span style="font-size:.85rem;color:var(--t6-green-dark);font-weight:600;margin-top:auto;">Learn More &rarr;</span>
        </a>

        <a href="hvac-system-replacement.html" class="t6-card" style="text-decoration:none;color:inherit;display:flex;flex-direction:column;padding:1.5rem;background:#fff;border:1px solid var(--t6-hairline);border-radius:10px;">
          <h4 style="font-family:var(--font-display);font-weight:700;color:var(--t6-ink);margin-bottom:.35rem;">HVAC System Replacement</h4>
          <p style="color:var(--t6-muted);font-size:.88rem;line-height:1.5;margin:0 0 1rem;">High-efficiency, variable-speed heat pump replacements in Naples.</p>
          <span style="font-size:.85rem;color:var(--t6-green-dark);font-weight:600;margin-top:auto;">Learn More &rarr;</span>
        </a>
      </div>
    </div>
  </section>

  <!-- CONTACT & ESTIMATE SECTION -->
  <section id="contact" class="t6-section" style="padding:4.5rem 0;">
    <div class="t6-container">
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:3.5rem;align-items:start;">
        <div>
          <span class="t6-pill" style="margin-bottom:.75rem;">Fast Local Dispatch</span>
          <h2 style="font-family:var(--font-display);font-size:clamp(1.75rem,3vw,2.4rem);font-weight:700;color:var(--t6-ink);margin-bottom:1rem;">
            Schedule {svc['service_name']} in Naples, FL
          </h2>
          <p style="color:var(--t6-muted);font-size:1.05rem;line-height:1.6;margin-bottom:1.5rem;">
            Contact Premium AC Solutions today for upfront pricing, rapid diagnostic arrival, and guaranteed satisfaction. Our trucks are in your neighborhood.
          </p>

          <div style="display:flex;flex-direction:column;gap:1.25rem;margin-bottom:2rem;">
            <div style="display:flex;gap:1rem;align-items:flex-start;">
              <span class="t6-icon-badge"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg></span>
              <div>
                <p style="margin:0;font-weight:700;color:var(--t6-ink);">Phone Number</p>
                <a href="tel:+12396861066" style="color:var(--t6-green-dark);font-size:1.2rem;font-weight:700;text-decoration:none;">(239) 686-1066</a>
              </div>
            </div>
            <div style="display:flex;gap:1rem;align-items:flex-start;">
              <span class="t6-icon-badge"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
              <div>
                <p style="margin:0;font-weight:700;color:var(--t6-ink);">Headquarters</p>
                <p style="margin:0;color:var(--t6-muted);"><a href="https://maps.google.com/?q=4389+Enterprise+Avenue,+Naples,+FL+34104" target="_blank" rel="noopener noreferrer" style="color:inherit;text-decoration:none;">4389 Enterprise Avenue, Naples, FL 34104</a></p>
              </div>
            </div>
            <div style="display:flex;gap:1rem;align-items:flex-start;">
              <span class="t6-icon-badge"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></span>
              <div>
                <p style="margin:0;font-weight:700;color:var(--t6-ink);">Hours of Operation</p>
                <p style="margin:0;color:var(--t6-muted);">Mon&ndash;Fri: 7AM &ndash; 7PM | Sat: 8AM &ndash; 4PM<br/><strong>24/7 Emergency Service Available</strong></p>
              </div>
            </div>
          </div>

          <div style="border-radius:12px;overflow:hidden;border:1px solid var(--t6-hairline);height:200px;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d114674.34114421114!2d-81.87222165!3d26.14728525!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88dae19b73c2d7ad%3A0x673f5ff111e1f167!2sNaples%2C%20FL!5e0!3m2!1sen!2sus!4v1700000000000!5m2!1sen!2sus" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map of Naples, Florida"></iframe>
          </div>
        </div>

        <div style="background:#fff;border:1px solid var(--t6-hairline);border-radius:14px;padding:2rem;box-shadow:0 15px 35px rgba(23,34,7,.06);">
          <h3 style="font-family:var(--font-display);font-size:1.35rem;font-weight:700;color:var(--t6-ink);margin:0 0 1rem;">
            Request Service Estimate
          </h3>
          <p style="color:var(--t6-muted);font-size:.9rem;line-height:1.5;margin-bottom:1.5rem;">
            Fill out the form below or call <a href="tel:+12396861066" style="color:var(--t6-green-dark);font-weight:700;text-decoration:none;">(239) 686-1066</a> for immediate response.
          </p>

          <form data-rl-lead style="display:flex;flex-direction:column;gap:1.15rem;">
            <div>
              <label style="display:block;font-size:.85rem;font-weight:600;color:var(--t6-ink);margin-bottom:.35rem;">Full Name</label>
              <input type="text" name="name" required placeholder="John Smith" style="width:100%;padding:.75rem .95rem;border:1px solid var(--t6-hairline);border-radius:8px;font-size:.95rem;background:var(--t6-band);" />
            </div>
            <div>
              <label style="display:block;font-size:.85rem;font-weight:600;color:var(--t6-ink);margin-bottom:.35rem;">Phone Number</label>
              <input type="tel" name="phone" required placeholder="(239) 000-0000" style="width:100%;padding:.75rem .95rem;border:1px solid var(--t6-hairline);border-radius:8px;font-size:.95rem;background:var(--t6-band);" />
            </div>
            <div>
              <label style="display:block;font-size:.85rem;font-weight:600;color:var(--t6-ink);margin-bottom:.35rem;">Email Address</label>
              <input type="email" name="email" required placeholder="john@example.com" style="width:100%;padding:.75rem .95rem;border:1px solid var(--t6-hairline);border-radius:8px;font-size:.95rem;background:var(--t6-band);" />
            </div>
            <div>
              <label style="display:block;font-size:.85rem;font-weight:600;color:var(--t6-ink);margin-bottom:.35rem;">Describe the Issue</label>
              <textarea name="message" rows="3" placeholder="Tell us what is happening with your AC system..." style="width:100%;padding:.75rem .95rem;border:1px solid var(--t6-hairline);border-radius:8px;font-size:.95rem;background:var(--t6-band);"></textarea>
            </div>
            <button type="submit" class="t6-btn t6-btn-primary" style="width:100%;padding:.9rem;font-size:1.05rem;font-weight:700;">
              Send Request &rarr;
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="t6-band-ink" style="position:relative;padding:4.5rem 0 2rem;margin-top:3rem;">
  <div class="t6-container" style="position:relative;">
    <div style="display:grid;gap:2.5rem;grid-template-columns:1.4fr 1fr 1fr 1fr;">
      <div>
        <a href="index.html" style="display:inline-block;text-decoration:none;margin-bottom:1.25rem;" aria-label="Premium AC Solutions">
            <img src="assets/images/logo-white.png" alt="Premium AC Solutions Logo" width="214" height="50"
              style="height:50px;width:auto;max-width:220px;object-fit:contain;display:block;" />
          </a>
        <hr class="t6-hr-green" style="margin:0 0 1rem;" />
        <p style="color:rgba(255,255,255,.78);max-width:340px;font-size:.95rem;line-height:1.7;">Licensed, insured hvac pros serving local homes and businesses with same-day response and a real workmanship warranty.</p>
        <div style="margin-top:1.25rem;display:flex;flex-wrap:wrap;gap:.6rem;" data-social-links>
          <a href="#" data-social="facebook" aria-label="Facebook" style="color:#fff;display:inline-flex;width:36px;height:36px;border:1px solid rgba(255,255,255,.25);border-radius:50%;align-items:center;justify-content:center;text-decoration:none;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95c5.05-.5 9-4.76 9-9.95"/></svg>
          </a>
          <a href="#" data-social="instagram" aria-label="Instagram" style="color:#fff;display:inline-flex;width:36px;height:36px;border:1px solid rgba(255,255,255,.25);border-radius:50%;align-items:center;justify-content:center;text-decoration:none;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2m-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.39 5.61 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.61 18.39 4 16.4 4zm9.65 1.5a1.25 1.25 0 0 1 1.25 1.25A1.25 1.25 0 0 1 17.25 8A1.25 1.25 0 0 1 16 6.75a1.25 1.25 0 0 1 1.25-1.25M12 7a5 5 0 0 1 5 5a5 5 0 0 1-5 5a5 5 0 0 1-5-5a5 5 0 0 1 5-5m0 2a3 3 0 0 0-3 3a3 3 0 0 0 3 3a3 3 0 0 0 3-3a3 3 0 0 0-3-3"/></svg>
          </a>
          <a href="#" data-social="x" aria-label="X/Twitter" style="color:#fff;display:inline-flex;width:36px;height:36px;border:1px solid rgba(255,255,255,.25);border-radius:50%;align-items:center;justify-content:center;text-decoration:none;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M10.488 14.651L15.25 21h7l-7.858-10.478L20.93 3h-2.65l-5.117 5.886L8.75 3h-7l7.51 10.015L2.32 21h2.65zM16.25 19L5.75 5h2l10.5 14z"/></svg>
          </a>
          <a href="#" data-social="linkedin" aria-label="LinkedIn" style="color:#fff;display:inline-flex;width:36px;height:36px;border:1px solid rgba(255,255,255,.25);border-radius:50%;align-items:center;justify-content:center;text-decoration:none;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93zM6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37z"/></svg>
          </a>
          <a href="#" data-social="youtube" aria-label="YouTube" style="color:#fff;display:inline-flex;width:36px;height:36px;border:1px solid rgba(255,255,255,.25);border-radius:50%;align-items:center;justify-content:center;text-decoration:none;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          </a>
          <a href="#" data-social="tiktok" aria-label="TikTok" style="color:#fff;display:inline-flex;width:36px;height:36px;border:1px solid rgba(255,255,255,.25);border-radius:50%;align-items:center;justify-content:center;text-decoration:none;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5.7 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1.74-.1z"/></svg>
          </a>
          <a href="#" data-social="pinterest" aria-label="Pinterest" style="color:#fff;display:inline-flex;width:36px;height:36px;border:1px solid rgba(255,255,255,.25);border-radius:50%;align-items:center;justify-content:center;text-decoration:none;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.373 0 0 5.372 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738.098.119.112.224.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24 12 24c6.627 0 12-5.373 12-12 0-6.628-5.373-12-12-12z"/></svg>
          </a>
        </div>
      </div>

      <div>
        <p style="color:#fff;font-family:var(--font-display);font-weight:600;font-size:1rem;margin:0 0 1rem;">Contact</p>
        <hr class="t6-hr-green" style="margin:0 0 1rem;" />
        <div style="color:rgba(255,255,255,.85);font-size:.92rem;line-height:1.7;">
          <p style="margin:0 0 .4rem;"><a href="tel:+12396861066" style="color:#fff;text-decoration:none;font-weight:600;">(239) 686-1066</a></p>
          <p style="margin:0 0 .4rem;"><a href="https://maps.google.com/?q=4389+Enterprise+Avenue,+Naples,+FL+34104" target="_blank" rel="noopener noreferrer" style="color:rgba(255,255,255,.85);text-decoration:none;" title="View Premium AC Solutions on Google Maps">4389 Enterprise Avenue, Naples, FL 34104</a></p>
          <p style="margin:0;">Mon&ndash;Fri: 7AM &ndash; 7PM<br/>Sat: 8AM &ndash; 4PM<br/>24/7 Emergency</p>
        </div>
      </div>

      <div>
        <p style="color:#fff;font-family:var(--font-display);font-weight:600;font-size:1rem;margin:0 0 1rem;">Services</p>
        <hr class="t6-hr-green" style="margin:0 0 1rem;" />
        <ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.5rem;font-size:.92rem;">
{footer_service_links}
          <li><a href="services.html" class="t6-link-grow t6-link-grow--on-ink" style="color:var(--t6-green);">View All &rarr;</a></li>
        </ul>
      </div>

      <div>
        <p style="color:#fff;font-family:var(--font-display);font-weight:600;font-size:1rem;margin:0 0 1rem;">Quick Links</p>
        <hr class="t6-hr-green" style="margin:0 0 1rem;" />
        <ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.5rem;font-size:.92rem;">
          <li><a href="about.html" style="color:rgba(255,255,255,.85);text-decoration:none;">About Us</a></li>
          <li><a href="locations.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Service Areas</a></li>
          <li><a href="hvac-bayshore-arts-district.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Bayshore Arts District</a></li>
          <li><a href="hvac-aqualane-shores.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Aqualane Shores</a></li>
          <li><a href="hvac-royal-harbor.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Royal Harbor</a></li>
          <li><a href="hvac-port-royal.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Port Royal</a></li>
          <li><a href="hvac-park-shore.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Park Shore</a></li>
          <li><a href="blog.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Blog</a></li>
          <li><a href="contact.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Contact</a></li>
          <li><a href="privacy-policy.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Privacy Policy</a></li>
        </ul>
      </div>
    </div>

    <div style="margin-top:3rem;padding-top:1.5rem;border-top:1px solid rgba(255,255,255,.12);display:flex;flex-wrap:wrap;justify-content:space-between;gap:1rem;align-items:center;color:rgba(255,255,255,.6);font-size:.85rem;">
      <p style="margin:0;">&copy; 2026 Premium AC Solutions. Licensed &amp; insured. All rights reserved.</p>
      <p style="margin:0;display:flex;gap:1rem;align-items:center;">
        <span style="display:inline-flex;gap:6px;align-items:center;">
          <span style="font-family:var(--font-display);font-weight:700;color:var(--t6-green);">VISA</span>
          <span style="font-family:var(--font-display);font-weight:700;color:var(--t6-green);">MC</span>
          <span style="font-family:var(--font-display);font-weight:700;color:var(--t6-green);">AMEX</span>
          <span style="font-family:var(--font-display);font-weight:700;color:var(--t6-green);">CASH</span>
        </span>
      </p>
    </div>
  </div>
  <style>
    @media (max-width: 900px) {{
      footer.t6-band-ink > .t6-container > div:first-child {{ grid-template-columns: 1fr 1fr !important; }}
    }}
    @media (max-width: 600px) {{
      footer.t6-band-ink > .t6-container > div:first-child {{ grid-template-columns: 1fr !important; }}
    }}
  </style>
</footer>

<div class="t6-mobile-cta" role="region" aria-label="Mobile call to action">
  <a href="tel:+12396861066" class="t6-mobile-cta__call">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
    Call (239) 686-1066
  </a>
  <a href="#contact" class="t6-mobile-cta__quote">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
    Get Quote
  </a>
</div>
<div class="t6-rail" role="region" aria-label="Quick contact rail">
  <a href="tel:+12396861066">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
    Call
  </a>
  <a href="#contact">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
    Quote
  </a>
</div>
    <script src="https://unpkg.com/sal.js"></script>
    <script src="assets/js/main.js"></script>
  </body>
</html>
"""
    return content

for svc in SERVICES:
    html = build_service_page(svc)
    with open(svc["filename"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {svc['filename']} ({len(html)} bytes)")

print("All 4 service pages successfully generated.")
