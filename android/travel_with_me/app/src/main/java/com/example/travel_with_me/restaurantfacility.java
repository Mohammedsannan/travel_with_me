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
public class restaurantfacility extends AppCompatActivity {
    ListView l1;
    ArrayList<String> name,image,description,fcid;
    String url;
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_restaurantfacility);
        l1=findViewById(R.id.l1);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        url = "http://" + sh.getString("ip", "") + ":5000/resfacility_android";
        RequestQueue queue = Volley.newRequestQueue(restaurantfacility.this);
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {
                    JSONArray ar = new JSONArray(response);
                    name = new ArrayList<>();
                    image = new ArrayList<>();
                    description = new ArrayList<>();
                    fcid= new ArrayList<>();
                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        name.add(jo.getString("name"));
                        image.add(jo.getString("image"));
                        description.add(jo.getString("description"));
                        fcid.add(jo.getString("fcid"));
                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new custom_facility(restaurantfacility.this, name,image,description,fcid));
//                    l1.setOnItemClickListener(view_menu.this);
                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }
            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(restaurantfacility.this, "err" + error, Toast.LENGTH_SHORT).show();
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

