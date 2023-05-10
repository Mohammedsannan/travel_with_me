package com.example.travel_with_me;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
public class recommendation extends AppCompatActivity {
    ImageView m1,m2,m3;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recommendation);
        m1=findViewById(R.id.imageView2);
        m2=findViewById(R.id.imageView3);
        m3=findViewById(R.id.imageView4);
        m1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i=new Intent(getApplicationContext(),recommendationrestaurant.class);
                startActivity(i);
            }
        });
        m2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i=new Intent(getApplicationContext(),recommendationresort.class);
                startActivity(i);
            }
        });
        m3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(getApplicationContext(), recommendationtourist.class);
                startActivity(i);
            }
        });

    }
}