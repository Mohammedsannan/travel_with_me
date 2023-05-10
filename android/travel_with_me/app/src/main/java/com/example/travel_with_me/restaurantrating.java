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
import android.widget.RatingBar;
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
public class restaurantrating extends AppCompatActivity {
    EditText e1;
    Button b1;
    RatingBar rtng;
    SharedPreferences sh;
    String url;
    String rating,review;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_restaurantrating);
        e1=findViewById(R.id.e);
        rtng=findViewById(R.id.ratingBar3);
        b1=findViewById(R.id.button4);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                rating=String.valueOf(rtng.getRating());
                review=e1.getText().toString();
                RequestQueue queue = Volley.newRequestQueue(restaurantrating.this);
                url = "http://" + sh.getString("ip", "") + ":5000/restaurantrating_android";
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
                                Intent ik = new Intent(getApplicationContext(),userhome.class);
                                startActivity(ik);
                            } else {
                                Toast.makeText(restaurantrating.this, "Invalid", Toast.LENGTH_SHORT).show();
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
                        params.put("uid",sh.getString("lid",""));
                        params.put("rid",getIntent().getStringExtra("rid"));
                        params.put("rating",rating);
                        params.put("review",review);
                        return params;
                    }
                };
                queue.add(stringRequest);
            }
        });

    }
}