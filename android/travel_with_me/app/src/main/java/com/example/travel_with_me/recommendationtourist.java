package com.example.travel_with_me;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.SearchView;
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
public class recommendationtourist extends AppCompatActivity {
    ListView list5;
    SearchView sv;
    ArrayList<String> place,image,description,tid,latitude,longitude,rating;
    String url;
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recommendationtourist);
        list5=findViewById(R.id.l3);
        sv=findViewById(R.id.s3);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        url = "http://" + sh.getString("ip", "") + ":5000/viewrcmdtourist_android";
        RequestQueue queue = Volley.newRequestQueue(recommendationtourist.this);
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {
                    JSONArray ar = new JSONArray(response);
                    place = new ArrayList<>();
                    image = new ArrayList<>();
                    description = new ArrayList<>();
                    tid= new ArrayList<>();
                    latitude= new ArrayList<>();
                    longitude= new ArrayList<>();
                    rating= new ArrayList<>();

                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        place.add(jo.getString("place"));
                        image.add(jo.getString("image"));
                        description.add(jo.getString("description"));
                        latitude.add(jo.getString("latitude"));
                        longitude.add(jo.getString("longitude"));
                        rating.add(jo.getString("rating"));
                        tid.add(jo.getString("tid"));
                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);
                    list5.setAdapter(new custom_touristplace(recommendationtourist.this,place,image,description,latitude,longitude,tid,rating));
//                    l1.setOnItemClickListener(view_menu.this);
                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }
            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(recommendationtourist.this, "err" + error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @NonNull
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("lid",sh.getString("lid",""));
                params.put("lati",LocationService.lati);
                params.put("longi",LocationService.logi);
                return params;
            }
        };
        queue.add(stringRequest);
    }

//    @Override
//    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
//        Intent in=new Intent(getApplicationContext(),restaurantmore.class);
//        in.putExtra("rid",rid.get(i));
//        in.putExtra("image",image.get(i));
//        in.putExtra("name",name.get(i));
//        in.putExtra("place",place.get(i));
//        startActivity(in);
//    }
}

