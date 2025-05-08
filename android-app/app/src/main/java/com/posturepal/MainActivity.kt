package com.postureguardian

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val statusTextView: TextView = findViewById(R.id.statusTextView)
        
        // Simulate posture detection - could be integrated with BLE or EMG classification
        val isSlouching = detectSlouching() // Replace with actual slouching detection logic

        if (isSlouching) {
            // Show red "lock" screen (you can expand this with full-screen overlay or modal)
            window.decorView.setBackgroundColor(resources.getColor(android.R.color.holo_red_light))
            statusTextView.text = "Fix Your Posture!"
        } else {
            window.decorView.setBackgroundColor(resources.getColor(android.R.color.white))
            statusTextView.text = "You're all straight!"
        }
    }

    private fun detectSlouching(): Boolean {
        // Simulate slouching detection
        // Replace with BLE or ML-based posture classification result
        return true // Example: Always slouching for now
    }
}