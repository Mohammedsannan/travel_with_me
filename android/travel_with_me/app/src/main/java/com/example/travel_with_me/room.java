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
public class room extends AppCompatActivity {
    ListView list3;
    ArrayList<String> roomno,image,type,amount;
    String url;
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_room);
        list3=findViewById(R.id.l3);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        url = "http://" + sh.getString("ip", "") + ":5000/roomresort_android";
        RequestQueue queue = Volley.newRequestQueue(room.this);
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {
                    JSONArray ar = new JSONArray(response);
                    roomno= new ArrayList<>();
                    image = new ArrayList<>();
                    amount = new ArrayList<>();
                    type = new ArrayList<>();
                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        roomno.add(jo.getString("roomno"));
                        image.add(jo.getString("image"));
                        type.add(jo.getString("type"));
                        amount.add(jo.getString("amount"));

                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    list3.setAdapter(new custom_room(room.this, roomno,image,type,amount));
//                    l1.setOnItemClickListener(view_menu.this);
                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }
            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(room.this, "err" + error, Toast.LENGTH_SHORT).show();
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

