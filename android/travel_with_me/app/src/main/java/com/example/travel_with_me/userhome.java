package com.example.travel_with_me;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.view.Menu;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;


import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import com.google.android.material.navigation.NavigationView;

import androidx.annotation.NonNull;


import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.drawerlayout.widget.DrawerLayout;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;


public class userhome extends AppCompatActivity  implements NavigationView.OnNavigationItemSelectedListener{



    ImageButton B1,B2,B3,B4,B5;
    ImageView I1;
    TextView T1,t2;
    SharedPreferences sh;
    String url,name,photo;
    ListView L1;

    ArrayList<String>heading,content;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userhome);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        View headerView = navigationView.getHeaderView(0);

        T1 = (TextView) headerView.findViewById(R.id.txt1);

//        View linearLayout=navigationView.inflateHeaderView(R.layout.nav_header_home);
        if(android.os.Build.VERSION.SDK_INT>9)
        {
            StrictMode.ThreadPolicy policy=new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }


//        T1.setText("xcxcvv");

//T1.setText("ffffffff");

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        view_user();

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();

//        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);


        navigationView.setNavigationItemSelectedListener(this);



    }

    private void view_user() {
        RequestQueue queue = Volley.newRequestQueue(userhome.this);
        url = "http://"+sh.getString("ip", "")+":5000/identifyuser_android";

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {
                    JSONObject json = new JSONObject(response);
                    String name = json.getString("nm");
                    T1.setText(name);

                } catch (JSONException e) {
                    e.printStackTrace();
                    Toast.makeText(userhome.this, ""+e, Toast.LENGTH_SHORT).show();

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

                params.put("lid",sh.getString("lid",""));
                return params;
            }
        };
        queue.add(stringRequest);

//

    }



    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.userhome, menu);
        return true;
    }


    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        int id= item.getItemId();
        if(id==R.id.restaurant)
        {
            Intent i=new Intent(getApplicationContext(),restaurant.class);
            startActivity(i);
        }
        if(id==R.id.resort)
        {
            Intent i=new Intent(getApplicationContext(),resort.class);
            startActivity(i);
        }
        if(id==R.id.touristplace)
        {
            Intent i=new Intent(getApplicationContext(),touristplace.class);
            startActivity(i);
        }
        if(id==R.id.recommended)
        {
            Intent i=new Intent(getApplicationContext(),recommendation.class);
            startActivity(i);
        }
        if(id==R.id.logout)
        {
            Intent i=new Intent(getApplicationContext(),login.class);
            startActivity(i);
        }if(id==R.id.complaints)
        {
            Intent i=new Intent(getApplicationContext(),complaints.class);
            startActivity(i);
        }if(id==R.id.reply)
        {
            Intent i=new Intent(getApplicationContext(),viewreply.class);
            startActivity(i);
        }if(id==R.id.feedback)
        {
            Intent i=new Intent(getApplicationContext(),feedback.class);
            startActivity(i);
        }


        return false;
    }
}