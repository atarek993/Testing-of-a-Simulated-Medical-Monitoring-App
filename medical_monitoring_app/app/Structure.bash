medical_monitoring_app/
├── app/                                # Main application code
│   ├── __init__.py                     # Initializes the `app` package
│   ├── biosignals.py                   # Handles heart rate, blood pressure, and oxygen saturation
│   ├── device.py                       # Simulates the wearable device functionality
│   ├── emergency_service.py            # Manages emergency contact and alert logic
│   ├── data_logger.py                  # Handles logging of biosignal data
│   ├── monitoring_workflow.py                          # Implements the monitoring workflow logic
├── tests/                              # Test files
│   ├── unit_tests/                     # Unit test files
│   │   ├── __init__.py                 # Initializes the `unit_tests` package
│   │   ├── test_biosignals.py          # Unit tests for the Biosignals class
│   │   ├── test_device.py              # Unit tests for the Device class
│   │   ├── test_emergency_service.py   # Unit tests for the EmergencyService class
│   │   ├── test_data_logger.py         # Unit tests for the DataLogger class
│   ├── integration_tests/              # Integration test files
│   │   ├── __init__.py                 # Initializes the `integration_tests` package
│   │   ├── test_monitoring_workflow.py # Integration tests for monitoring workflow
│   │   └── test_data_logging.py        # Integration tests for data logging and alerts
│   ├── system_tests/                   # System test files
│   │   ├── __init__.py                 # Initializes the `system_tests` package
│   │   └── test_complete_workflow.py   # End-to-end system tests
│   ├── performance_tests/              # Performance test files
│   │   ├── __init__.py                 # Initializes the `performance_tests` package
│   │   └── test_performance.py         # Performance tests for high-frequency updates
│   └── __init__.py                     # Shared fixtures and test setup
├── docs/                               # Documentation files
│   ├── test_case_documentation.md/doc  # Detailed test case documentation
│   └── Names.md                       # Overview of the project
