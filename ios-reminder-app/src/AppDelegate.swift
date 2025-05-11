import UserNotifications

func requestNotificationPermissions() {
    UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) { granted, error in
        if let error = error {
            print("Permission error: \(error.localizedDescription)")   
        } else {
            print("Permission granted: \(granted)")
        }
    }
}