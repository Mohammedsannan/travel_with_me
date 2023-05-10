package com.example.travel_with_me;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.GridView;
import android.widget.ImageView;
import android.widget.RatingBar;
import android.widget.TextView;
import java.util.ArrayList;
public class custom_touristplace extends BaseAdapter {
    private Context context;
    ArrayList<String> a;
    ArrayList<String> b;
    ArrayList<String> c;
    ArrayList<String> d;
    ArrayList<String> e;
    ArrayList<String> f;
    ArrayList<String> g;

    SharedPreferences sh;
    public custom_touristplace(Context applicationContext, ArrayList<String> a, ArrayList<String> b, ArrayList<String> c, ArrayList<String> d, ArrayList<String> e,ArrayList<String> f,ArrayList<String> g) {
        // TODO Auto-generated constructor stub
        this.context=applicationContext;
        this.a=a;
        this.b=b;
        this.c=c;
        this.d=d;
        this.e=e;
        this.f=f;
        this.g=g;

        sh=PreferenceManager.getDefaultSharedPreferences(applicationContext);
    }
    @Override
    public int getCount() {
        // TODO Auto-generated method stub
        return a.size();
    }
    @Override
    public Object getItem(int arg0) {
        // TODO Auto-generated method stub
        return null;
    }
    @Override
    public long getItemId(int arg0) {
        // TODO Auto-generated method stub
        return 0;
    }
    @Override
    public int getItemViewType(int arg0) {
        // TODO Auto-generated method stub
        return 0;
    }
    @Override
    public View getView(int position, View convertview, ViewGroup parent) {
        // TODO Auto-generated method stub
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        View gridView;
        if(convertview==null)
        {
            gridView=new View(context);
            gridView=inflator.inflate(R.layout.activity_custom_touristplace, null);

        }
        else
        {
            gridView=(View)convertview;
        }
//        TextView tv1=(TextView)gridView.findViewById(R.id.tvroom);
        ImageView i1=(ImageView) gridView.findViewById(R.id.imgaprtmnt);
        TextView tv2=(TextView)gridView.findViewById(R.id.tvhall);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView12);
        Button b1=(Button) gridView.findViewById(R.id.button6);
        Button b2=(Button) gridView.findViewById(R.id.button7);
        RatingBar ratingBar=(RatingBar) gridView.findViewById(R.id.ratingBar6);
        ratingBar.setRating(Float.parseFloat(g.get(position)));
        ratingBar.setIsIndicator(true);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(android.content.Intent.ACTION_VIEW,
                        Uri.parse("http://maps.google.com/maps?q="+d.get(position)+","+e.get(position)));
                context.startActivity(intent);            }
        });

        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(context,touristplacerating.class);
                intent.putExtra("tpid",f.get(position));
                context.startActivity(intent);

            }
        });

        if(android.os.Build.VERSION.SDK_INT>9)
        {
            StrictMode.ThreadPolicy policy=new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }
        java.net.URL thumb_u;
        try {
            //thumb_u = new java.net.URL("http://192.168.43.57:5000/static/photo/flyer.jpg");
            thumb_u = new java.net.URL("http://"+sh.getString("ip","")+":5000/media/"+b.get(position));
            Drawable thumb_d = Drawable.createFromStream(thumb_u.openStream(), "src");
            i1.setImageDrawable(thumb_d);
        }

        catch (Exception e)
        {
            Log.d("errsssssssssssss",""+e);
        }
//        tv1.setText(a.get(position));
        tv2.setText(a.get(position));
        tv3.setText(c.get(position));
//        tv4.setText(e.get(position));

//        tv1.setTextColor(Color.BLACK);
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);
//        tv4.setTextColor(Color.BLACK);












        return gridView;

    }

}





