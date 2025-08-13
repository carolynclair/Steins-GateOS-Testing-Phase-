#!/usr/bin/env python3
"""
Test suite for Steins;GateOS
Tests the core functionality and commands of the operating system.
"""

import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
import importlib.util

# Import the OS module
spec = importlib.util.spec_from_file_location("steins_gate_os", "steins_gate_os.py")
steins_gate_os = importlib.util.module_from_spec(spec)
spec.loader.exec_module(steins_gate_os)

class TestSteinsGateOS(unittest.TestCase):
    """Test cases for Steins;GateOS functionality"""
    
    def setUp(self):
        """Set up test environment"""
        self.os_instance = steins_gate_os.SteinsGateOS()
        
    def test_initialization(self):
        """Test OS initialization"""
        self.assertEqual(self.os_instance.current_user, "okabe")
        self.assertAlmostEqual(self.os_instance.world_line, 1.130205, places=6)
        self.assertTrue(self.os_instance.running)
        self.assertEqual(len(self.os_instance.lab_members), 8)
        self.assertEqual(len(self.os_instance.future_gadgets), 8)
        self.assertEqual(len(self.os_instance.dmail_history), 0)
        
    def test_command_parsing(self):
        """Test command parsing functionality"""
        # Test basic command
        command, args = self.os_instance.parse_command("help")
        self.assertEqual(command, "help")
        self.assertEqual(args, [])
        
        # Test command with arguments
        command, args = self.os_instance.parse_command("dmail Hello World")
        self.assertEqual(command, "dmail")
        self.assertEqual(args, ["Hello", "World"])
        
        # Test empty command
        command, args = self.os_instance.parse_command("")
        self.assertIsNone(command)
        self.assertEqual(args, [])
        
    def test_lab_members_data(self):
        """Test lab members data integrity"""
        expected_members = ["Okabe Rintaro", "Makise Kurisu", "Mayuri Shiina", 
                          "Itaru Hashida", "Suzuha Amane", "Moeka Kiryu", 
                          "Ruka Urushibara", "Faris NyanNyan"]
        
        actual_members = [member["name"] for member in self.os_instance.lab_members.values()]
        
        for expected in expected_members:
            self.assertIn(expected, actual_members)
            
    def test_future_gadgets_data(self):
        """Test future gadgets data integrity"""
        expected_gadgets = ["Bit Particle Cannon", "Bamboo-copter Camera", 
                          "Televised Ouija Board", "Moad Snake", "Upa", 
                          "36th Cyborg", "CRT Editor", "Phone Microwave"]
        
        actual_gadgets = [gadget["name"] for gadget in self.os_instance.future_gadgets.values()]
        
        for expected in expected_gadgets:
            self.assertIn(expected, actual_gadgets)
            
    def test_dmail_functionality(self):
        """Test D-Mail system functionality"""
        # Test valid D-Mail
        initial_count = len(self.os_instance.dmail_history)
        initial_world_line = self.os_instance.world_line
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.cmd_dmail(["Test", "message"])
            
        self.assertEqual(len(self.os_instance.dmail_history), initial_count + 1)
        self.assertEqual(self.os_instance.dmail_history[0], "Test message")
        
        # World line should have changed slightly
        self.assertNotEqual(self.os_instance.world_line, initial_world_line)
        
        # Test D-Mail too long
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.cmd_dmail(["This", "is", "a", "very", "long", "message", "that", 
                                      "exceeds", "the", "36", "byte", "limit", "for", "D-Mail"])
            output = mock_stdout.getvalue()
            
        self.assertIn("ERROR: Message too long!", output)
        
    def test_command_execution(self):
        """Test command execution"""
        # Test valid command
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.execute_command("help", [])
            output = mock_stdout.getvalue()
            
        self.assertIn("AVAILABLE COMMANDS", output)
        
        # Test invalid command
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.execute_command("invalid", [])
            output = mock_stdout.getvalue()
            
        self.assertIn("Command 'invalid' not found", output)
        
    def test_time_command(self):
        """Test time command output"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.cmd_time([])
            output = mock_stdout.getvalue()
            
        self.assertIn("TIME OPERATIONS", output)
        self.assertIn("World Line:", output)
        self.assertIn("α Attractor Field", output)
        
    def test_status_command(self):
        """Test status command output"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.cmd_status([])
            output = mock_stdout.getvalue()
            
        self.assertIn("SYSTEM STATUS", output)
        self.assertIn("OPERATIONAL", output)
        self.assertIn("OKABE", output)
        
    def test_quote_command(self):
        """Test quote command functionality"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.cmd_quote([])
            output = mock_stdout.getvalue()
            
        self.assertIn("RANDOM QUOTE", output)
        # Should contain at least one quote
        self.assertTrue(len(output) > 100)
        
    def test_lab_command(self):
        """Test lab command output"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.cmd_lab([])
            output = mock_stdout.getvalue()
            
        self.assertIn("LAB MEMBER DATABASE", output)
        self.assertIn("Okabe Rintaro", output)
        self.assertIn("Makise Kurisu", output)
        
    def test_gadgets_command(self):
        """Test gadgets command output"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.cmd_gadgets([])
            output = mock_stdout.getvalue()
            
        self.assertIn("FUTURE GADGET DATABASE", output)
        self.assertIn("Phone Microwave", output)
        self.assertIn("CLASSIFIED", output)
        
    def test_divergence_command(self):
        """Test divergence command functionality"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.cmd_divergence([])
            output = mock_stdout.getvalue()
            
        self.assertIn("WORLD LINE ANALYSIS", output)
        self.assertIn("Current Divergence:", output)
        self.assertIn("α (Alpha)", output)
        
    def test_prompt_generation(self):
        """Test command prompt generation"""
        prompt = self.os_instance.get_prompt()
        self.assertIn("Lab-", prompt)
        self.assertIn("@okabe:~$", prompt)
        
    def test_exit_command(self):
        """Test exit command functionality"""
        self.assertTrue(self.os_instance.running)
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.os_instance.cmd_exit([])
            output = mock_stdout.getvalue()
            
        self.assertFalse(self.os_instance.running)
        self.assertIn("El Psy Kongroo", output)

class TestSteinsGateOSIntegration(unittest.TestCase):
    """Integration tests for Steins;GateOS"""
    
    def test_multiple_dmails(self):
        """Test sending multiple D-Mails"""
        os_instance = steins_gate_os.SteinsGateOS()
        initial_world_line = os_instance.world_line
        
        # Send multiple D-Mails
        with patch('sys.stdout', new_callable=StringIO):
            os_instance.cmd_dmail(["First", "message"])
            os_instance.cmd_dmail(["Second", "message"])
            os_instance.cmd_dmail(["Third", "message"])
            
        self.assertEqual(len(os_instance.dmail_history), 3)
        self.assertNotEqual(os_instance.world_line, initial_world_line)
        
    def test_dmail_history_display(self):
        """Test D-Mail history display"""
        os_instance = steins_gate_os.SteinsGateOS()
        
        # Add some D-Mails
        with patch('sys.stdout', new_callable=StringIO):
            os_instance.cmd_dmail(["Test", "message", "one"])
            os_instance.cmd_dmail(["Test", "message", "two"])
            
        # Check history display
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            os_instance.cmd_dmail([])  # No arguments shows history
            output = mock_stdout.getvalue()
            
        self.assertIn("Test message one", output)
        self.assertIn("Test message two", output)
        
    def test_command_case_sensitivity(self):
        """Test that commands are case sensitive (as expected for OS)"""
        os_instance = steins_gate_os.SteinsGateOS()
        
        # Test lowercase command (should work)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            os_instance.execute_command("help", [])
            output = mock_stdout.getvalue()
            
        self.assertIn("AVAILABLE COMMANDS", output)
        
        # Test uppercase command (should fail)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            os_instance.execute_command("HELP", [])
            output = mock_stdout.getvalue()
            
        self.assertIn("Command 'HELP' not found", output)

if __name__ == "__main__":
    print("Running Steins;GateOS Test Suite...")
    print("=" * 50)
    
    # Run the tests
    unittest.main(verbosity=2)