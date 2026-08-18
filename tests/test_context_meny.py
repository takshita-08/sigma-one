from datetime import datetime, timedelta
from logging import config

from playwright.sync_api import expect

from utils import config
from utils.config import BASE_URL, DEB_TO_UPGRADE, UPDATE_URL_API, BASE_URL_API, UPDATE_URL


def test_context_menu(select_device,immediate_reboot=False):
    print("🔹 test_context_menu: Test started and test details page loaded.")
    quick_command_button = select_device.page.get_by_role("button", name="Quick Command")
    
    quick_command_button.click()
    upload_debug_logs_option = select_device.page.get_by_role("listitem", name="Upload Debug Logs")
    upload_debug_logs_option.click()
    upload_start_date_option = select_device.page.get_by_test_id("testStartDate") 
    upload_end_date_option = select_device.page.get_by_test_id("testEndDate")
    upload_start_time_option = select_device.page.locator("#mt-testStartTime")
    upload_end_time_option = select_device.page.locator("#mt-testEndTime")
    upload_ok_button = select_device.page.locator('button[form="uploadDebugLogsForm"]', has_text="Fetch")
    upload_start_date_option.fill(datetime.now().strftime("%m/%d/%Y"))
    select_device.page.keyboard.press("Enter")
    upload_end_date_option.fill(datetime.now().strftime("%m/%d/%Y"))
    select_device.page.keyboard.press("Enter")
    upload_start_time_option.fill("10:10")
    select_device.page.keyboard.press("Enter")
    upload_end_time_option.fill("11:10")
    select_device.page.keyboard.press("Enter")
    upload_ok_button.click()
    # run_automatic_script_option = select_device.page.get_by_role("listitem", name="Run Automatic Script")
    # run_automatic_script_endpoint = select_device.page.get_by_test_id("testEndpoint")
    # run_automatic_script_timeout = select_device.page.get_by_test_id("testTimeout")
    # run_automatic_script_scenario_id = select_device.page.get_by_test_id("testScenarioId")
    # run_automatic_script_position_id = select_device.page.get_by_test_id("testPositionId")
    # run_automatic_script_file_prefix = select_device.page.get_by_test_id("testFilePrefix")
    # run_automatic_script_file_prefix_as_script_name = select_device.page.get_by_test_id("testFilePrefixAsScriptNameName")
    # run_automatic_script_script_search = select_device.page.get_by_test_id("testScriptSearch")
    # run_automatic_script_ok_button = select_device.page.locator('button[form="runAutomationScriptModal"]', has_text="Run")
    
    # live_monitoring_dashboard_id = select_device.page.locator("#mt-testDashboardId")
    # dashboard_list_ok_button = select_device.page.locator('button[form="AllDashboardList"]', has_text="OK")
    # dt_script_confirmation_popup = select_device.page.locator(".confirmationPopup").get_by_text("Test is already running on", exact=False)
    # dt_script_confirmation_confirm_button = select_device.page.get_by_role("button", name="Confirm")

    # run_automatic_script_option.click()
    # run_automatic_script_endpoint.fill("https://example.com/api")
    # run_automatic_script_timeout.fill("60")
    # run_automatic_script_scenario_id.fill("1")
    # run_automatic_script_position_id.fill("1")
    # run_automatic_script_file_prefix_as_script_name.uncheck()
    # run_automatic_script_file_prefix.fill("TestPrefix")
    # run_automatic_script_script_search.fill("actionDT")
    # run_automatic_script_ok_button.click()
    # select_device.page.wait_for_timeout(3000)  # Wait for the script to start and dashboard options to load
    # if dt_script_confirmation_popup.is_visible():
    #     dt_script_confirmation_confirm_button.click()
    # # select_device.page.wait_for_timeout(5000)  # Wait for the script to start and dashboard options to load
    # live_monitoring_dashboard_id.fill("Lab Automation")
    # select_device.page.keyboard.press("Enter")
    # dashboard_list_ok_button.click()




    # at_commands_option = select_device.page.get_by_role("listitem", name="AT Commands")
    # at_command_textbox = select_device.page.get_by_test_id("testATCommands")
    # at_command_send_button = select_device.page.get_by_role("button", name="Send")
    # at_command_delete_history = select_device.page.get_by_role("button", name="Delete History")
    # at_commands_option.click()
    # at_command_textbox.fill("AT+CSQ")
    # at_command_send_button.click()
    # at_command_delete_history.click()


    # select_device.page.get_by_role("listitem", name="Device Configuration").click()
    # combo=select_device.page.locator('#deviceConfigurationForm table tbody tr td:nth-child(2) .search-select__input')
    # combo.click()
    # combo.fill("Unassigned")
    # select_device.page.keyboard.press("Enter")
    # okbtn=select_device.page.locator('button[form="deviceConfigurationForm"]', has_text="OK")
    # okbtn.click()
    select_device.page.pause()

    # file_manager_option = select_device.page.get_by_role("listitem", name="File Manager")
    # file_manager_option.click()

    # expect(file_manager_option).to_be_visible(timeout=5000)

    # select_device.page.get_by_role("listitem", name="Reboot Settings").click()
    # if not select_device.page.locator("#mt-testEnableReboot").is_checked():
    #         select_device.page.locator(".on-off-toggle").click()
    # if immediate_reboot:
    #     select_device.page.get_by_test_id("testImmediateReboot").check()
    # else:
    #     select_device.page.get_by_test_id("testImmediateReboot").uncheck()      
    #     reboot_time_textbox = select_device.page.get_by_role("textbox", name="hh:mm")
    #     reboot_time_textbox.click()
    #     print(reboot_time_textbox.inner_text())
    #     print("🔹 Reboot time textbox clicked.")
    #     reboot_time_textbox.fill("10:30")
    #     print("🔹 Reboot time filled in textbox.")
    #     select_device.page.get_by_test_id("testTime").get_by_role("button", name="OK").click()

    #     select_device.page.locator('button[form="rebootSettingsForm"]').click()       # ok_btn.click()
    #     print("🔹 OK button clicked to set reboot time.")

    # select_device.page.get_by_role("listitem", name="GPS Coordinate").click()
    # dialog = select_device.page.locator(".modal-content").filter(
    # has=select_device.page.get_by_text("GPS Coordinate"))

    # dialog.get_by_role("button", name="Cancel").click()
    # cancel_button = select_device.page.get_by_role("button", name="Cancel").locator(":visible")
    # # cancel_button.click()
    # select_device.page.get_by_role("listitem", name="Assign Schedule").click()
    # checkbox= select_device.page.locator('.form-group').locator('input[type="checkbox"]').nth(0)
    # if not checkbox.is_checked():
    #     checkbox.click()
    # # select_device.page.locator("tbody tr").nth(0).get_by_role("checkbox").check()
    # # select_device.page.get_by_role('dialog', name='Assign Schedule').get_by_role('combobox').click()
    # # schedule = select_device.page.get_by_role("cell", name="Unassigned").get_by_role("combobox")
    # # schedule = select_device.page.locator("tbody tr td:nth-child(3)").get_by_role("combobox")
    # schedule = select_device.page.locator("td .search-and-select").get_by_role("combobox")
    # schedule.click()
    # schedule.fill("Ping_Long")
    # select_device.page.keyboard.press("Enter")
    # select_device.page.locator('button[form="deviceAssignScheduleForSigmaoneForm"]').click()
    # select_device.page.locator('.assign-schedule-modal .mobile-dropdown button').click()

    # Add assertions to verify the context menu functionality
    # For example, you can check if the context menu is visible when right-clicking on an element
    # or if the correct options are displayed in the context menu.

def test_file_manager_context_menu(context_menu):
    print("🔹 test_file_manager_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_file_manager()

def test_upload_debug_logs_context_menu(context_menu):
    print("🔹 test_upload_debug_logs_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    current_date = datetime.now().strftime("%m/%d/%Y")
    current_time = datetime.now().strftime("%H:%M")
    start_time = (datetime.now() - timedelta(minutes=15)).strftime("%H:%M")
    timestamp = current_date + " " + current_time
    print(f"🔹 Current date: {current_date}, Current time: {current_time}, Start time: {start_time}, timestamp : {timestamp}")
    context_menu.select_upload_debug_logs(current_date,current_date, start_time, current_time)
    timestamp_cell = (context_menu.page.locator("#mt-loadingDone").get_by_text(timestamp, exact=False))
    assert "debugLogs" in context_menu.page.url, "Failed to navigate to debug logs page"
    expect(timestamp_cell).to_be_visible(timeout=6000)  # Wait for the timestamp cell to be visible after applying the filter

def test_reboot_settings_context_menu(context_menu):
    print("🔹 test_reboot_settings_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    reboot_time = (datetime.now() + timedelta(minutes=2)).strftime("%H:%M")
    print(f"🔹 Reboot time set to: {reboot_time}")
    context_menu.select_reboot_settings(reboot_time)
    success_toast = context_menu.page.get_by_text("Reboot settings saved successfully", exact=False)
    expect(success_toast).to_be_visible(timeout=5000)  # Wait for the success toast to be visible
    # context_menu.page.pause()

def test_reboot_settings_context_menu_immediate(context_menu):
    print("🔹 test_reboot_settings_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_reboot_settings()
    success_toast = context_menu.page.get_by_text("Reboot settings saved successfully", exact=False)
    expect(success_toast).to_be_visible(timeout=5000)


def test_assign_schedule_context_menu(context_menu):
    print("🔹 test_assign_schedule_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_assign_schedule()

def test_device_settings_context_menu(context_menu):
    print("🔹 test_device_settings_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_device_setting(DEB_TO_UPGRADE)
    context_menu.page.pause()

def test_run_adb_shell_context_menu(context_menu):
    print("🔹 test_run_adb_shell_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_run_adb_shell()
    assert config.BASE_URL == UPDATE_URL, "Failed to override BASE_URL for update URL test"

def test_update_url_context_menu(context_menu, override_config_for_update_url,select_device):
    print("🔹 test_update_url_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_update_url(UPDATE_URL_API)
    select_device.open_context_menu()
    select_device.select_update_url(BASE_URL_API)
    # monkeypatch.setattr(config, BASE_URL, UPDATE_URL)
    # context_menu.page.goto(BASE_URL_API, wait_until="domcontentloaded")




def test_network_detach_attach_context_menu(context_menu):
    print("🔹 test_network_detach_attach_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_network_detach_attach()

def test_license_upgrade_context_menu(context_menu):
    print("🔹 test_license_upgrade_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_license_upgrade()

def test_wifi_context_menu(context_menu):
    print("🔹 test_wifi_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_wifi()

def test_airplane_mode_context_menu(context_menu):
    print("🔹 test_airplane_mode_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_airplane_mode()

def test_gps_coordinate_context_menu(context_menu):
    print("🔹 test_gps_coordinate_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_gps_coordinate()

def test_device_configuration_context_menu(context_menu):
    print("🔹 test_device_configuration_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_device_configuration()

def test_at_commands_context_menu(context_menu):
    print("🔹 test_at_commands_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_at_commands()

def test_run_automatic_script_context_menu(context_menu):
    print("🔹 test_run_automatic_script_context_menu: Test started and test details page loaded.")
    context_menu.open_context_menu()
    context_menu.select_run_automatic_script()