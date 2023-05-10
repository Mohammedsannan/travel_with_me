package com.example.travel_with_me;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.RatingBar;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class restaurantmore extends AppCompatActivity {
    ImageView m1;
    TextView t1,t2,t3,t4,t5;
    Button b,b2,b3,b4;
    RatingBar rb;
    SharedPreferences sh;
    String rid,image,name,place,url;
    String email,phn,addrress,lattitude,longitude;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_restaurantmore);
        m1=findViewById(R.id.img);
        b=findViewById(R.id.b3);
        b2=findViewById(R.id.b4);
        b3=findViewById(R.id.b5);
        b4=findViewById(R.id.b6);
        t1=findViewById(R.id.textView3);
        t2=findViewById(R.id.textView4);
        t3=findViewById(R.id.textView5);
        t4=findViewById(R.id.textView6);
        t5=findViewById(R.id.textView7);
        rb=findViewById(R.id.ratingBar5);
        rid=getIntent().getStringExtra("rid");
        image=getIntent().getStringExtra("image");
        place=getIntent().getStringExtra("place");
        name=getIntent().getStringExtra("name");
        t1.setText(name);
        t2.setText(place);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        restaurant_rating();
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(),menu.class);
                intent.putExtra("rid",rid);
                startActivity(intent);
            }
        });
        b4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(android.content.Intent.ACTION_VIEW,
                        Uri.parse("http://maps.google.com/maps?q="+lattitude+","+longitude));
                startActivity(intent);

            }
        });
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(),restaurantfacility.class);
                intent.putExtra("rid",rid);
                startActivity(intent);

            }
        });
        b3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(),restaurantrating.class);
                intent.putExtra("rid",rid);
                startActivity(intent);

            }
        });


//        Toast.makeText(restaurantmore.this, "more..." +image+""+place, Toast.LENGTH_SHORT).show();
        url = "http://" + sh.getString("ip", "") + ":5000/viewmore_restaurant";
        RequestQueue queue = Volley.newRequestQueue(restaurantmore.this);
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {
                    JSONArray ar = new JSONArray(response);


                        JSONObject jo = ar.getJSONObject(0);
                        email=jo.getString("email");
                        phn=jo.getString("phonenumber");
                        addrress=jo.getString("address");
                        lattitude=jo.getString("lattitude");
                        longitude=jo.getString("longitude");

                    t3.setText(email);
                    t4.setText(phn);
                    t5.setText(addrress);


                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(restaurantmore.this, "err" + error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @NonNull
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("rid",getIntent().getStringExtra("rid"));
                return params;
            }
        };
        queue.add(stringRequest);
        if(android.os.Build.VERSION.SDK_INT>9)
        {
            StrictMode.ThreadPolicy policy=new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }
        java.net.URL thumb_u;
        try {
            //thumb_u = new java.net.URL("http://192.168.43.57:5000/static/photo/flyer.jpg");
            thumb_u = new java.net.URL("http://"+sh.getString("ip","")+":5000/media/"+image);
            Drawable thumb_d = Drawable.createFromStream(thumb_u.openStream(), "src");
            m1.setImageDrawable(thumb_d);
        }
        catch (Exception e)
        {
            Log.d("errsssssssssssss",""+e);
        }





    }

    private void restaurant_rating() {
        url = "http://" + sh.getString("ip", "") + ":5000/view_restaurant_rating";
        RequestQueue queue = Volley.newRequestQueue(restaurantmore.this);
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {
                    JSONObject json = new JSONObject(response);
                    String rating = json.getString("task");
                    rb.setRating(Float.parseFloat(rating));
//                    rb.setFocusable(false);



                    rb.setIsIndicator(true);


//                    l1.setOnItemClickListener(view_menu.this);
                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }
            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(restaurantmore.this, "err" + error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @NonNull
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("rid", getIntent().getStringExtra("rid"));
                return params;
            }
        };
        queue.add(stringRequest);
    }
}

