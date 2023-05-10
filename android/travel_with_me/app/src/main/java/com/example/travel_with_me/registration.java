package com.example.travel_with_me;


import androidx.appcompat.app.AppCompatActivity;

import android.app.DatePickerDialog;
import android.app.DownloadManager;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Build;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.example.travel_with_me.MainActivity;
import com.example.travel_with_me.R;

import org.json.JSONException;
import org.json.JSONObject;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

public class registration extends AppCompatActivity {
    EditText F,A,ph,g,pass,eml;

    RadioButton r1,r2;
    Button b1;
    String fullname,address,gender,phone,email,password,url;
    SharedPreferences sh;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);
        F=findViewById(R.id.F);
        A=findViewById(R.id.A);
        r1=findViewById(R.id.r1);
        r2=findViewById(R.id.r2);
        b1=findViewById(R.id.b1);


        ph=findViewById(R.id.ph);
        eml=findViewById(R.id.eml);
        pass=findViewById(R.id.pass);
        if(r1.isChecked())
        {
            gender=r1.getText().toString();
        }
        else
        {
            gender=r2.getText().toString();
        }



        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                fullname=F.getText().toString();
                address=A.getText().toString();
                phone=ph.getText().toString();
                email=eml.getText().toString();


                password=pass.getText().toString();


                if (r1.isChecked()) {
                    gender = r1.getText().toString();

                } else
                {
                    gender = r2.getText().toString();
                }
//                if (firstname.equalsIgnoreCase("")) {
//                    F.setError("enter your first name");
//                }
//                else if (!firstname.matches("^[a-zA-Z]*$")) {
//                    F.setError(" characters  allowed");
//                    F.requestFocus();
//                }
//
//
//                else if (lastname.equalsIgnoreCase("")) {
//                    L.setError("enter your last name");
//                }
//                else if (!lastname.matches("^[a-zA-Z]*$")) {
//                    L.setError(" characters  allowed");
//                    L.requestFocus();
//                }
//                else if (gender.equalsIgnoreCase("")) {
//                    r1.setError("select gender");
//                }
//                else if (address.equalsIgnoreCase("")) {
//                    A.setError("enter your address");
//                }
//
//                else if (phone.equalsIgnoreCase("")) {
//                    ph.setError("enter your phone");
//                }
//                else if (phone.length() != 10) {
//                    ph.setError(" numbers  allowed");
//                }
//                else if (dob.equalsIgnoreCase("")) {
//                    D.setError("enter date of birth");
//                }
//
//
//
//                else if (email.equalsIgnoreCase("")) {
//                    eml.setError("enter your  email");
//                }
//
//                else if (!Patterns.EMAIL_ADDRESS.matcher(email).matches()){
//                    eml.setError("enter valid email");
//                    eml.requestFocus();
//                }
//                else if (email.matches(("^[a-z]*$"))) {
//                    eml.setError(" characters  allowed");
//                }
//                else if (username.equalsIgnoreCase("")) {
//                    u.setError("enter your  username");
//                }
//                else  if (password.equalsIgnoreCase("")) {
//                    pass.setError("enter your  password");
//                }
//                else if (!username.matches("^[a-z]*$")) {
//                    u.setError(" characters  allowed");
//                }
//                else {

                    RequestQueue queue = Volley.newRequestQueue(registration.this);
                    url = "http://"+sh.getString("ip", "")+":5000/userregister";

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
                                    Toast.makeText(registration.this, "registered successfully ", Toast.LENGTH_SHORT).show();

                                    Intent ik = new Intent(getApplicationContext(), login.class);
                                    startActivity(ik);

                                } else {

                                    Toast.makeText(registration.this, "please try again", Toast.LENGTH_SHORT).show();

                                }
                            } catch (JSONException e) {
                                e.printStackTrace();
                                Toast.makeText(registration.this, ""+e, Toast.LENGTH_SHORT).show();

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

                            params.put("fullname", fullname);
                            params.put("address", address);
                            params.put("gender", gender);

                            params.put("phonenumber", phone);
                            params.put("email", email);

                            params.put("password", password);
                            return params;
                        }
                    };
                    queue.add(stringRequest);

//

            }
        });



    }


}