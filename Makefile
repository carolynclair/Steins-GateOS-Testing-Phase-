# Steins;GateOS Makefile
# Commands for running and testing the Future Gadget Laboratory OS

.PHONY: run test help clean install

# Default target
help:
	@echo "Steins;GateOS - Future Gadget Laboratory Operating System"
	@echo "=========================================================="
	@echo ""
	@echo "Available commands:"
	@echo "  make run       - Start Steins;GateOS"
	@echo "  make test      - Run the test suite"
	@echo "  make install   - Make the OS executable" 
	@echo "  make clean     - Clean up temporary files"
	@echo "  make help      - Show this help message"
	@echo ""
	@echo "El Psy Kongroo."

# Run the operating system
run: install
	@echo "Starting Steins;GateOS..."
	@echo "Initializing Future Gadget Laboratory systems..."
	@python3 steins_gate_os.py

# Run tests
test:
	@echo "Running Steins;GateOS Test Suite..."
	@echo "Testing timeline integrity..."
	@python3 test_steins_gate_os.py

# Make the OS executable
install:
	@chmod +x steins_gate_os.py
	@echo "Steins;GateOS is now executable."

# Clean up temporary files
clean:
	@echo "Cleaning up lab data..."
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.tmp" -delete 2>/dev/null || true
	@echo "Lab cleaned."

# Quick start target
start: run