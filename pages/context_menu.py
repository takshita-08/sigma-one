from utils.config import DEBUG_LOGS_URL
class ContextMenu:
    def __init__(self, page):
        self.page = page
        self.quick_command_button = self.page.get_by_role("button", name="Quick Command")
        self.file_manager_option = self.page.get_by_role("listitem", name="File Manager")
        self.upload_debug_logs_option = self.page.get_by_role("listitem", name="Upload Debug Logs")
        self.upload_start_date_option = self.page.get_by_test_id("testStartDate")
        self.upload_end_date_option = self.page.get_by_test_id("testEndDate")
        self.upload_start_time_option = self.page.locator("#mt-testStartTime")
        self.upload_end_time_option = self.page.locator("#mt-testEndTime")
        self.fetch_logs_button = self.page.get_by_role("button", name="Fetch Logs")
        self.upload_start_time_ok_button = self.page.locator(".MuiDialogActions-root").get_by_role("button", name="OK")
        self.upload_end_time_ok_button = self.page.locator(".MuiPickersLayout-actionBar").get_by_role("button", name="OK")
        self.filter_btn = self.page.locator("#mt-mt-filterBtn:visible")
        self.filter_clearBtn = self.page.locator("#mt-clearBtn")
        self.filter_apply = self.page.locator("#mt-filterBtn")


        self.stop_test_option = self.page.get_by_role("listitem", name="Stop Test")
        self.start_test_option = self.page.get_by_role("listitem", name="Start Test")
        self.reboot_settings_option = self.page.get_by_role("listitem", name="Reboot Settings")
        self.enable_reboot_toggle = self.page.locator("#mt-testEnableReboot")
        # self.enable_reboot_toggle = self.page.page.locator(".on-off-toggle")
        self.reboot_time_text = self.page.locator("#mt-testTime")
        # self.time_text= self.page.get_by_role("textbox", name="hh:mm")
        # self.hours_listbox = self.page.get_by_role("listbox", name="Select hours")
        # self.minutes_listbox = self.page.get_by_role("listbox", name="Select minutes")
        self.reboot_time_ok_button = self.page.locator(".MuiPickersLayout-actionBar").get_by_role("button", name="OK")
        self.immediate_reboot_checkbox = self.page.get_by_test_id("testImmediateReboot")
        # self.reboot_time_ok_button = self.page.get_by_test_id("testTime").get_by_role("button", name="OK")
        self.reboot_ok_button = self.page.locator('button[form="rebootSettingsForm"]', has_text="OK")
        
        self.assign_schedule_option = self.page.get_by_role("listitem", name="Assign Schedule")
        self.assign_schedule_checkbox = self.page.locator('.form-group').locator('input[type="checkbox"]').nth(0)
        self.select_schedule = self.page.locator("td .search-and-select").get_by_role("combobox")
        self.schedule_ok_button = self.page.locator('button[form="deviceAssignScheduleForSigmaoneForm"]', has_text="OK")

        
        self.device_setting_option = self.page.get_by_role("listitem", name="Device Setting")
        self.deb_name = self.page.locator("#mt-testDebId")
        self.is_apply_immediate = self.page.get_by_test_id("testIsApplyImmediate")
        self.device_setting_ok_button = self.page.locator('button[form="deviceSettingConfigForm"]', has_text="OK")

        self.run_adb_option = self.page.get_by_role("listitem", name="Run ADB")
        self.adb_command_radio = self.page.get_by_test_id("ADB Command")
        self.adb_script_radio = self.page.get_by_test_id("ADB Script")
        self.shell_radio = self.page.get_by_test_id("Shell")
        self.adb_command_textbox = self.page.get_by_test_id("testAdbCommand")
        self.adb_script_combobox = self.page.get_by_role("combobox", name="testScriptId")
        self.shell_textbox = self.page.get_by_test_id("testShell")
        self.run_adb_ok_button = self.page.locator('button[form="adbCommandForm"]', has_text="OK")
        
        self.update_url_option = self.page.get_by_role("listitem", name="Update URL")
        self.update_url_textbox = self.page.get_by_test_id("testUpdateUrl")
        self.update_url_ok_button = self.page.locator('button[form="updateURLForm"]', has_text="Save")
        self.network_detach_attach_option = self.page.get_by_role("listitem", name="Network Detach Attach")
        self.license_upgrade_option = self.page.get_by_role("listitem", name="License Upgrade")
        self.wifi_option = self.page.locator(".subcontext-arrow").first
        self.wifi_on_option = self.page.get_by_test_id("WiFion")
        self.wifi_off_option = self.page.get_by_test_id("WiFioff")
        self.airplane_option = self.page.locator("#dropdown-basic > .subcontext-arrow").first
        self.airplane_on_option = self.page.get_by_test_id("flighton")
        self.airplane_off_option = self.page.get_by_test_id("flightoff")
        self.gps_coordinate_option = self.page.get_by_role("listitem", name="GPS Coordinate")
        self.latitude_textbox = self.page.get_by_test_id("testLatitude")
        self.longitude_textbox = self.page.get_by_test_id("testLongitude")
        self.gps_coordinate_ok_button = self.page.locator('button[form="gpsCoordinateForm"]', has_text="OK")
        self.device_configuration_option = self.page.get_by_role("listitem", name="Device Configuration")
        self.device_configuration_target_device = self.page.locator('#deviceConfigurationForm table tbody tr td:nth-child(2) .search-select__input')
        self.device_configuration_network_adapter = self.page.locator('#deviceConfigurationForm table tbody tr td:nth-child(3) .search-select__input')
        self.device_configuration_logmask = self.page.locator('#deviceConfigurationForm table tbody tr td:nth-child(4) .search-select__input')
        self.device_configuration_ok_button = self.page.locator('button[form="deviceConfigurationForm"]', has_text="OK")
# locator("div").filter(has_text="Centra-SDTest is already").nth(3)

        
        
        self.at_commands_option = self.page.get_by_role("listitem", name="AT Commands")
        self.at_command_textbox = self.page.get_by_test_id("testATCommands")
        self.at_command_send_button = self.page.get_by_role("button", name="Send")
        self.at_command_delete_history = self.page.get_by_role("button", name="Delete History")
        
        self.run_automatic_script_option = self.page.get_by_role("listitem", name="Run Automatic Script")
        self.run_automatic_script_endpoint = self.page.get_by_test_id("testEndpoint")
        self.run_automatic_script_timeout = self.page.get_by_test_id("testTimeout")
        self.run_automatic_script_scenario_id = self.page.get_by_test_id("testScenarioId")
        self.run_automatic_script_position_id = self.page.get_by_test_id("testPositionId")
        self.run_automatic_script_file_prefix = self.page.get_by_test_id("testFilePrefix")
        self.run_automatic_script_file_prefix_as_script_name = self.page.get_by_test_id("testFilePrefixAsScriptNameName")
        self.run_automatic_script_script_search = self.page.get_by_test_id("testScriptSearch")
        self.run_automatic_script_ok_button = self.page.locator('button[form="runAutomationScriptModal"]', has_text="Run")
        self.dt_script_confirmation_popup = self.page.locator(".confirmationPopup").get_by_text("Test is already running on", exact=False)
        self.dt_script_confirmation_confirm_button = self.page.get_by_role("button", name="Confirm")

        self.live_monitoring_dashboard_id = self.page.locator("#mt-testDashboardId")
        self.dashboard_list_ok_button = self.page.locator('button[form="AllDashboardList"]', has_text="OK")


    def open_context_menu(self):
        # Simulate right-click on the specified element to open the context menu
        self.quick_command_button.click()

    def select_file_manager(self):
        self.file_manager_option.click()
    
    def select_upload_debug_logs(self, start_date, end_date, start_time, end_time):
        self.upload_debug_logs_option.click()
        self.upload_start_date_option.click()
        self.upload_start_date_option.fill(start_date)
        self.page.keyboard.press("Enter")
        self.upload_end_date_option.click()
        self.upload_end_date_option.fill(end_date)
        self.page.keyboard.press("Enter")
        self.upload_start_time_option.click()
        self.upload_start_time_option.fill(start_time)
        self.page.keyboard.press("Enter")
        self.upload_start_time_ok_button.click()
        self.upload_end_time_option.click()
        self.upload_end_time_option.fill(end_time)
        self.page.keyboard.press("Enter")
        self.upload_end_time_ok_button.click()
        # self.page.pause()
        self.fetch_logs_button.click()
        self.page.goto(DEBUG_LOGS_URL, wait_until="domcontentloaded")
        self.page.wait_for_timeout(30000)
        self.filter_btn.click()
        self.filter_clearBtn.click()
        self.filter_apply.click()
          # Refresh the page to update the state after fetching logs
    
    def select_stop_test(self, stop_test):
        self.stop_test_option.click()
    
    def select_start_test(self, start_test):
        self.start_test_option.click()
    
    def select_reboot_settings(self, reboot_time=None):
        self.reboot_settings_option.click()
        if not self.enable_reboot_toggle.is_checked():
             self.enable_reboot_toggle.click()
        if reboot_time is not None:
            self.immediate_reboot_checkbox.uncheck()      
            self.reboot_time_text.click()
            self.reboot_time_text.fill(reboot_time)
            # self.reboot_time_ok_button.click()
            self.page.keyboard.press("Enter")
            self.reboot_time_ok_button.click()
        else:
            self.immediate_reboot_checkbox.check()
            
        self.reboot_ok_button.click()
    
    def select_assign_schedule(self, schedule_name):
        self.assign_schedule_option.click()
        if not self.assign_schedule_checkbox.is_checked():
            self.assign_schedule_checkbox.check()
        self.select_schedule.click().fill(schedule_name)
        self.page.keyboard.press("Enter")
        self.schedule_ok_button.click()

    def select_device_setting(self, deb_name):
        self.device_setting_option.click()
        self.deb_name.fill(deb_name)
        self.page.keyboard.press("Enter")
        if not self.is_apply_immediate.is_checked():
            self.is_apply_immediate.check()
        self.device_setting_ok_button.click()
    
    def select_run_adb_shell(self,adb_type,command_or_script):
        self.run_adb_option.click()
        if adb_type == "command":
            self.adb_command_radio.check()
            self.adb_command_textbox.click().fill(command_or_script)
        elif adb_type == "script":
            self.adb_script_radio.check()
            self.adb_script_combobox.select_option(command_or_script)
        elif adb_type == "shell":
            self.shell_radio.check()
            self.shell_textbox.click().fill(command_or_script)
        self.run_adb_ok_button.click()
    
    def select_update_url(self, updated_url):
        self.update_url_option.click()
        self.update_url_textbox.click()
        self.update_url_textbox.fill(updated_url)
        self.update_url_ok_button.click()
        # self.page.pause()
    
    def select_network_detach_attach(self):
        self.network_detach_attach_option.click()
    
    def select_license_upgrade(self):
        self.license_upgrade_option.click()
    
    def select_wifi(self, is_wifi_on):
        self.wifi_option.click()
        if is_wifi_on:
            self.wifi_on_option.click()
        else:            
            self.wifi_off_option.click()
    
    def select_airplane_mode(self, is_airplane_on):
        self.airplane_option.click()
        if is_airplane_on:
            self.airplane_on_option.click()
        else:
            self.airplane_off_option.click()
    
    def select_gps_coordinate(self, latitude, longitude):
        self.gps_coordinate_option.click()
        self.latitude_textbox.click().fill(latitude)
        self.longitude_textbox.click().fill(longitude)
        self.gps_coordinate_ok_button.click()
    
    def select_device_configuration(self, target_device=None, network_adapter=None, logmask=None):
        self.device_configuration_option.click()
        if target_device:
            self.device_configuration_target_device.click().fill(target_device)
            self.page.keyboard.press("Enter")
        if network_adapter:
            self.device_configuration_network_adapter.click().fill(network_adapter)
            self.page.keyboard.press("Enter")
        if logmask:
            self.device_configuration_logmask.click().fill(logmask)
            self.page.keyboard.press("Enter")
        self.device_setting_ok_button.click()
    
    def select_at_commands(self,at_command):
        self.at_commands_option.click()
        self.at_command_textbox.click().fill(at_command)
        self.at_command_send_button.click()
    
    def select_run_automatic_script(self, dt_script,dashboard_name,endpoint=None, timeout=None, scenario_id=None, position_id=None, file_prefix=None, file_prefix_as_script_name=False):
        self.run_automatic_script_option.click()
        if endpoint:
            self.run_automatic_script_endpoint.click().fill(endpoint)
        if timeout:
            self.run_automatic_script_timeout.click().fill(timeout)
        if scenario_id:
            self.run_automatic_script_scenario_id.click().fill(scenario_id)
        if position_id:
            self.run_automatic_script_position_id.click().fill(position_id)

        if file_prefix_as_script_name:
            self.run_automatic_script_file_prefix_as_script_name.check()
        else:
            self.run_automatic_script_file_prefix_as_script_name.uncheck()
            self.run_automatic_script_file_prefix.click().fill(file_prefix)

        script_name = self.page.get_by_text(dt_script, exact=True)
        script_name.click()
        self.page.wait_for_timeout(3000)
        if self.dt_script_confirmation_popup.is_visible():
            self.dt_script_confirmation_confirm_button.click()
        self.run_automatic_script_ok_button.click()
        self.live_monitoring_dashboard_id.click().fill(dashboard_name)
        self.dashboard_list_ok_button.click()


