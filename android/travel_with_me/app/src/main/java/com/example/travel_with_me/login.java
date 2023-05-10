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
public class login extends AppCompatActivity {
    EditText e1,e2;
    Button b1,b2;
    String u,p,url;
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        e1=findViewById(R.id.username);
        e2=findViewById(R.id.password);
        b1=findViewById(R.id.loginButton);
        b2=findViewById(R.id.reg);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i=new Intent(getApplicationContext(),registration.class);
                startActivity(i);
            }
        });
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                u= e1.getText().toString();
                p= e2.getText().toString();
                RequestQueue queue = Volley.newRequestQueue(login.this);
                url = "http://" + sh.getString("ip", "") + ":5000/logins";

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
                                String lid = json.getString("id");
                                SharedPreferences.Editor edp = sh.edit();
                                edp.putString("lid", lid);
                                edp.commit();
                                Toast.makeText(login.this, "login successfully", Toast.LENGTH_SHORT).show();
                                Intent ik = new Intent(getApplicationContext(),userhome.class);
                                startActivity(ik);
                                Intent ik1= new Intent(getApplicationContext(),LocationService.class);
                                startService(ik1);
                            } else {
                                Toast.makeText(login.this, "Invalid username or password", Toast.LENGTH_SHORT).show();
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
                        params.put("username", u);
                        params.put("password", p);

                        return params;
                    }
                };
                queue.add(stringRequest);
            }
        });
    }
}