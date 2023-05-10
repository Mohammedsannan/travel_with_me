package com.example.travel_with_me;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class feedback extends AppCompatActivity {
    EditText e1;
    Button b1;
    SharedPreferences sh;
    String feed,url;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_feedback);
        e1=findViewById(R.id.editTextTextPersonName3);
        b1=findViewById(R.id.button5);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                feed=e1.getText().toString();
                RequestQueue queue = Volley.newRequestQueue(feedback.this);
                url = "http://" + sh.getString("ip", "") + ":5000/sendfeedback";

                // Request a string response from the provided URL.
                StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the response string.
                        Log.d("+++++++++++++++++", response);
                        try {
                            JSONObject json = new JSONObject(response);
                            String res = json.getString("task");
                            if (res.equalsIgnoreCase("success")) {

                                Toast.makeText(feedback.this, "send successfully", Toast.LENGTH_SHORT).show();
                                Intent ik = new Intent(getApplicationContext(),userhome.class);
                                startActivity(ik);

                            } else {
                                Toast.makeText(feedback.this, "Invalid username or password", Toast.LENGTH_SHORT).show();
                            }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
                    }
                }) {
                    @Override
                    protected Map<String, String> getParams() {
                        Map<String, String> params = new HashMap<String, String>();
                        params.put("feed", feed);
                        params.put("lid", sh.getString("lid",""));

                        return params;
                    }
                };
                queue.add(stringRequest);
            }
        });
    }
}